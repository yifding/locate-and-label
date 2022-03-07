import os
import argparse
import jsonlines
from functools import partial
from tqdm.contrib.concurrent import process_map
from tqdm import tqdm


def process_instance(instance, max_span_length=5, max_seq_length=100):
    asin = instance.get('asin', '')
    product_type = instance.get('product_type', '')
    tokens = instance["X_text"]
    tokens_lower = [token.lower() for token in tokens]
    tokens_lower = tokens_lower[:max_seq_length]

    gt_spans = []

    att = list(instance['Y_values'].keys())[0]
    attribute_values = instance['Y_values'][att]
    for i in range(len(tokens_lower) - 1):
        for j in range(i + 1, min(len(tokens_lower)+1, i+1+max_span_length)):
            select_tokens = tokens_lower[i:j]
            pred_text = ' '.join(select_tokens)

            if pred_text not in attribute_values:
                continue

            gt_span = {
                "start": i,
                "end": j,
                "type": att,
            }
            gt_spans.append(gt_span)

    gt_spans = sorted(gt_spans, key=lambda x: (x["start"], x["end"]))
    re_instance = {
        "asin": asin,
        "org_id": asin,
        "product_type": product_type,
        "entities": gt_spans,
        "tokens": tokens_lower,
        "pos": ["NN" for _ in range(len(tokens_lower))],
        "relations": {},
        "ltokens": {},
        "rtokens": {},
    }
    return re_instance


def prepare_test_data(
    input_file,
    output_file,
    max_span_length,
    max_seq_length,
):
    # input_file = "/scratch365/yding4/AVE_project/consumable/title_bullet/33att/sample_data_1/adatag/33_with_no_answer_ratio_0.0.train"
    # output_file = "/scratch365/yding4/AVE_project/consumable/title_bullet/33att/sample_data_1/end2end/train.jsonl"

    with jsonlines.open(input_file, 'r') as reader:
        instances = [instance for instance in reader]

    re_instances = process_map(
        partial(process_instance, max_span_length=max_span_length, max_seq_length=max_seq_length),
        instances,
        chunksize=1,
        max_workers=8,
    )
    # re_instances = []
    # for instance in tqdm(instances):
    #     re_instance = process_instance(instance, max_span_length=max_span_length, max_seq_length=max_seq_length)
    #     re_instances.append(re_instance)

    with jsonlines.open(output_file, 'w') as writer:
        writer.write_all(re_instances)


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        "--input_dir",
        required=True,
        # default="/yifad_ebs/consumable/clean_test_data/Color.gold"
        type=str,
    )
    parser.add_argument(
        "--output_dir",
        required=True,
        # default="/yifad_ebs/AVEQA_PyTorch/RUN_FILES/08_15_2021/qa_15att/train_qa_neg_1",
        type=str,
    )
    parser.add_argument(
        "--max_span_length",
        default=5,
        help="maximum length (number of words) of span",
        type=int,
    )
    parser.add_argument(
        "--max_seq_length",
        default=300,
        help="maximum length (number of words) of sequence",
        type=int,
    )
    parser.add_argument(
        "--test_att_list",
        required=True,
        # default="['ActiveIngredients','AgeRangeDescription','BatteryCellComposition','Brand','CaffeineContent','CapacityUnit','CoffeeRoastType','Color','DietType','DosageForm','EnergyUnit','FinishType','Flavor','FormulationType','HairType','Ingredients','ItemForm','ItemShape','LiquidContentsDescription','Material','MaterialFeature','MaterialTypeFree','PackageSizeName','Pattern','PatternType','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','TeaVariety','Variety']",
        type=eval,
    )

    args = parser.parse_args()
    assert os.path.isdir(args.input_dir)

    os.makedirs(args.output_dir, exist_ok=True)

    return args


def main():
    args = parse_args()
    for test_att in args.test_att_list:
        input_file = os.path.join(args.input_dir, f'{test_att}.gold')
        output_file = os.path.join(args.output_dir, f'{test_att}.json')
        prepare_test_data(
            input_file=input_file,
            output_file=output_file,
            max_span_length=args.max_span_length,
            max_seq_length=args.max_seq_length,
        )


if __name__ == "__main__":
    main()
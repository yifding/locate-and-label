import os
import json
import argparse


def raw_raw2raw(input_file, output_file, att):
    with open(input_file) as reader:
        d = json.load(reader)

    output_instances = dict()
    for index, instance in enumerate(d):
        tokens = instance['tokens']
        entities = instance['entities']
        tmp_instances = []
        for entity in entities:
            start, end, entity_type = entity['start'], entity['end'], entity['type']
            if entity_type == att:
                tmp_instance = ' '.join(tokens[start:end])
                tmp_instances.append(tmp_instance)
        output_instances[index] = tmp_instances

    with open(output_file, 'w') as writer:
        json.dump(output_instances, writer, indent=4)


def parse_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument(
        "--input_dir",
        required=True,
        # default="/yifad_ebs/consumable/clean_test_data/Color.gold"
        type=str,
    )
    parser.add_argument(
        "--test_att_list",
        required=True,
        # default="['ActiveIngredients','AgeRangeDescription','BatteryCellComposition','Brand','CaffeineContent','CapacityUnit','CoffeeRoastType','Color','DietType','DosageForm','EnergyUnit','FinishType','Flavor','FormulationType','HairType','Ingredients','ItemForm','ItemShape','LiquidContentsDescription','Material','MaterialFeature','MaterialTypeFree','PackageSizeName','Pattern','PatternType','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','TeaVariety','Variety']",
        type=eval,
    )

    args = parser.parse_args()
    assert os.path.isdir(args.input_dir)
    return args


def main():
    args = parse_args()
    input_dir = os.path.join(args.input_dir, 'raw_raw_prediction')
    assert os.path.isdir(input_dir)
    output_dir = os.path.join(args.input_dir, 'raw_prediction')
    os.makedirs(output_dir, exist_ok=True)

    for test_att in args.test_att_list:
        input_file = os.path.join(input_dir, f'{test_att}.json')
        output_file = os.path.join(output_dir, f'{test_att}.json')
        raw_raw2raw(
            input_file=input_file,
            output_file=output_file,
            att=test_att,
        )


if __name__ == "__main__":
    main()
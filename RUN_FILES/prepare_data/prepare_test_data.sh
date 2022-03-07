#!/bin/bash

#$-m abe
#$-M dyfdyf0125@gmail.com
#$-q gpu@qa-xp-001
#$-l gpu_card=4
#$-N CRC_ran_end2end

export PATH=/nfs/yding4/conda_envs/locate-and-label/bin:$PATH
export LD_LIBRARY_PATH=/nfs/yding4/conda_envs/locate-and-label/lib:$LD_LIBRARY_PATH

CODE=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/prepare_data/prepare_test_data.py

INPUT_DIR=/nfs/yding4/AVE_project/consumable/clean_test_data/
OUTPUT_DIR=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/prepare_data/test
MAX_SPAN_LENGTH=5
MAX_SEQ_LENGTH=100

# test on 15 att
TEST_ATT_LIST="['ActiveIngredients','AgeRangeDescription','Color','FinishType','Flavor','HairType','ItemForm','Material','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','Variety']"


/nfs/yding4/conda_envs/locate-and-label/bin/python ${CODE}   \
  --input_dir ${INPUT_DIR}    \
  --output_dir ${OUTPUT_DIR}  \
  --max_span_length ${MAX_SPAN_LENGTH}    \
  --max_seq_length ${MAX_SEQ_LENGTH}  \
  --test_att_list ${TEST_ATT_LIST}
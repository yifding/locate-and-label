#!/bin/bash

#$-m abe
#$-M dyfdyf0125@gmail.com
#$-q gpu@qa-xp-001
#$-l gpu_card=4
#$-N CRC_ran_end2end

export PATH=/nfs/yding4/conda_envs/locate-and-label/bin:$PATH
export LD_LIBRARY_PATH=/nfs/yding4/conda_envs/locate-and-label/lib:$LD_LIBRARY_PATH

CODE=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/prepare_data/process_raw_raw2raw.py

INPUT_DIR=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/train_33att

# test on 15 att
TEST_ATT_LIST="['ActiveIngredients','AgeRangeDescription','Color','FinishType','Flavor','HairType','ItemForm','Material','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','Variety']"


/nfs/yding4/conda_envs/locate-and-label/bin/python ${CODE}   \
  --input_dir ${INPUT_DIR}    \
  --test_att_list ${TEST_ATT_LIST}
#!/bin/bash

export PATH=/nfs/yding4/conda_envs/AVEQA_PyTorch2/bin:$PATH
export LD_LIBRARY_PATH=/nfs/yding4/conda_envs/AVEQA_PyTorch2/lib:$LD_LIBRARY_PATH

INPUT_DIR=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/train_33att
TEST_DIR=/nfs/yding4/AVE_project/consumable/clean_test_data
MODE="cascade"

# evaluate only on 15att
ATT_LIST="['ActiveIngredients','AgeRangeDescription','Color','FinishType','Flavor','HairType','ItemForm','Material','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','Variety']"

CODE=/nfs/yding4/AVE_project/AVEQA_PyTorch/AVEQA_PyTorch/cascade/inference/post_processing.py

/nfs/yding4/conda_envs/AVEQA_PyTorch2/bin/python \
  ${CODE} \
  --input_dir ${INPUT_DIR} \
  --test_dir ${TEST_DIR}  \
  --att_list ${ATT_LIST}  \
  --mode ${MODE}
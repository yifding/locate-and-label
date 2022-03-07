#!/bin/bash

#$-m abe
#$-M dyfdyf0125@gmail.com
#$-q gpu@qa-xp-001
#$-l gpu_card=4
#$-N CRC_ran_end2end

export PATH=/nfs/yding4/conda_envs/locate-and-label/bin:$PATH
export LD_LIBRARY_PATH=/nfs/yding4/conda_envs/locate-and-label/lib:$LD_LIBRARY_PATH

CODE_DIR=/nfs/yding4/AVE_project/locate-and-label

CONFIG=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/train_33att/33att_eval.config
YD_TEST_DIR=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/prepare_data/test
YD_TEST_ATT_LIST="['ActiveIngredients','AgeRangeDescription','Color','FinishType','Flavor','HairType','ItemForm','Material','ProductBenefit','Scent','SkinTone','SkinType','SpecialIngredients','TargetGender','Variety']"
YD_OUTPUT_DIR=/nfs/yding4/AVE_project/locate-and-label/RUN_FILES/train_33att/raw_raw_prediction

cd ${CODE_DIR}

/nfs/yding4/conda_envs/locate-and-label/bin/python identifier.py eval    \
    --config    ${CONFIG}   \
    --yd_test_dir   ${YD_TEST_DIR}    \
    --yd_test_att_list  ${YD_TEST_ATT_LIST}   \
    --yd_output_dir ${YD_OUTPUT_DIR}


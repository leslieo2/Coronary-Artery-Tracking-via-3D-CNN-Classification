rm train_save_d1_train.csv train_save_d1_val.csv

touch train_save_d1_train.csv
touch train_save_d1_val.csv

## 
cat negative/gp_19/d0_patch_info.csv > train_save_d1_train.csv
cat negative/gp_19/d2_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_19/d3_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_19/d4_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_19/d5_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_19/d6_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_19/d7_patch_info.csv >> train_save_d1_train.csv

cat positive/gp_100/d0_patch_info.csv > train_save_d1_train.csv
cat positive/gp_100/d2_patch_info.csv >> train_save_d1_train.csv
cat positive/gp_100/d3_patch_info.csv >> train_save_d1_train.csv
cat positive/gp_100/d4_patch_info.csv >> train_save_d1_train.csv
cat positive/gp_100/d5_patch_info.csv >> train_save_d1_train.csv
cat positive/gp_100/d6_patch_info.csv >> train_save_d1_train.csv
cat positive/gp_100/d7_patch_info.csv >> train_save_d1_train.csv

## 

cat negative/gp_19/d1_patch_info.csv > train_save_d1_val.csv
cat positive/gp_100/d1_patch_info.csv >> train_save_d1_val.csv

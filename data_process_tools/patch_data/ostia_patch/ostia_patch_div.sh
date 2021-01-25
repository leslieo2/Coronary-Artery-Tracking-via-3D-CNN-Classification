rm train_save_d1_train.csv train_save_d1_val.csv

touch train_save_d1_train.csv
touch train_save_d1_val.csv

## 
cat negative/gp_1/d0_patch_info.csv > train_save_d1_train.csv
cat negative/gp_1/d2_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_1/d3_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_1/d4_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_1/d5_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_1/d6_patch_info.csv >> train_save_d1_train.csv
cat negative/gp_1/d7_patch_info.csv >> train_save_d1_train.csv

cat postive/gp_1/d0_patch_info.csv > train_save_d1_train.csv
cat postive/gp_1/d2_patch_info.csv >> train_save_d1_train.csv
cat postive/gp_1/d3_patch_info.csv >> train_save_d1_train.csv
cat postive/gp_1/d4_patch_info.csv >> train_save_d1_train.csv
cat postive/gp_1/d5_patch_info.csv >> train_save_d1_train.csv
cat postive/gp_1/d6_patch_info.csv >> train_save_d1_train.csv
cat postive/gp_1/d7_patch_info.csv >> train_save_d1_train.csv

## 

cat negative/gp_1/d1_patch_info.csv > train_save_d1_val.csv
cat postive/gp_1/d1_patch_info.csv >> train_save_d1_val.csv

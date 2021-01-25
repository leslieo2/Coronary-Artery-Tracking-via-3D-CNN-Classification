rm train_save_d1_train.csv train_save_d1_val.csv

touch train_save_d1_train.csv
touch train_save_d1_val.csv

## 
cat offset/point_500_gp_1/d0_patch_info_500.csv > train_save_d1_train.csv
cat offset/point_500_gp_1/d2_patch_info_500.csv >> train_save_d1_train.csv
cat offset/point_500_gp_1/d3_patch_info_500.csv >> train_save_d1_train.csv
cat offset/point_500_gp_1/d4_patch_info_500.csv >> train_save_d1_train.csv
cat offset/point_500_gp_1/d5_patch_info_500.csv >> train_save_d1_train.csv
cat offset/point_500_gp_1/d6_patch_info_500.csv >> train_save_d1_train.csv
cat offset/point_500_gp_1/d7_patch_info_500.csv >> train_save_d1_train.csv

cat no_offset/point_500_gp_1/d0_patch_info_500.csv > train_save_d1_train.csv
cat no_offset/point_500_gp_1/d2_patch_info_500.csv >> train_save_d1_train.csv
cat no_offset/point_500_gp_1/d3_patch_info_500.csv >> train_save_d1_train.csv
cat no_offset/point_500_gp_1/d4_patch_info_500.csv >> train_save_d1_train.csv
cat no_offset/point_500_gp_1/d5_patch_info_500.csv >> train_save_d1_train.csv
cat no_offset/point_500_gp_1/d6_patch_info_500.csv >> train_save_d1_train.csv
cat no_offset/point_500_gp_1/d7_patch_info_500.csv >> train_save_d1_train.csv

## 

cat offset/point_500_gp_1/d1_patch_info_500.csv > train_save_d1_val.csv
cat no_offset/point_500_gp_1/d1_patch_info_500.csv >> train_save_d1_val.csv

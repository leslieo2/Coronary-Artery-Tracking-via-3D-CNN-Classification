import pandas as pd

size = 8


def get_csv_path(data_dir):
    files = []
    for i in range(size):
        f = '{0}d{1}_patch_info_500.csv'.format(data_dir, i)
        files.append(f)
    return files


def to_csv():
    no_offset_paths = get_csv_path(data_dir='no_offset/point_500_gp_1/')
    offset_paths = get_csv_path(data_dir='offset/point_500_gp_1/')
    all_csv = no_offset_paths + offset_paths
    print('all_csv: ', all_csv)
    no_offset_df = pd.DataFrame()
    idx = 0
    for csv in no_offset_paths:
        single_data_frame = pd.read_csv(csv)
        if idx == 0:
            no_offset_df = single_data_frame
        else:
            no_offset_df = pd.concat(
                [no_offset_df, single_data_frame], ignore_index=True)
        idx += 1

    offset_df = pd.DataFrame()
    idx = 0
    for csv in offset_paths:
        single_data_frame = pd.read_csv(csv)
        if idx == 0:
            offset_df = single_data_frame
        else:
            offset_df = pd.concat(
                [offset_df, single_data_frame], ignore_index=True)
        idx += 1
    no_offset_df_len = len(no_offset_df)
    offset_df = offset_df.sample(frac=1)[0:no_offset_df_len]

    total_df = pd.concat([no_offset_df, offset_df], ignore_index=True)
    total_df = total_df.sample(frac=1)
    n = len(total_df)
    # df = df[0:int(n//512)]
    # n = len(df)
    print('n={0}'.format(n))
    train, val = total_df[int(n/8):n], total_df[0:int(n/8)]
    print('train: {0}, val: {1}, rate: {2}.'.format(
        len(train), len(val), len(train) / len(val)))
    train.to_csv('train_save_d1_train.csv', index=0)
    val.to_csv('train_save_d1_val.csv', index=0)


to_csv()

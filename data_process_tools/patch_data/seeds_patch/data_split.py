import pandas as pd

size = 8


def get_csv_path(data_dir):
    files = []
    for i in range(size):
        f = '{0}d{1}_patch_info.csv'.format(data_dir, i)
        files.append(f)
    return files


def to_csv():
    negative_paths = get_csv_path(data_dir='negative/gp_19/')
    positive_paths = get_csv_path(data_dir='positive/gp_100/')
    all_csv = negative_paths + positive_paths
    print('all_csv: ', all_csv)

    negative_df = pd.DataFrame()
    idx = 0
    for csv in negative_paths:
        single_data_frame = pd.read_csv(csv)
        if idx == 0:
            negative_df = single_data_frame
        else:
            negative_df = pd.concat(
                [negative_df, single_data_frame], ignore_index=True)
        idx += 1

    positive_df = pd.DataFrame()
    idx = 0
    for csv in positive_paths:
        single_data_frame = pd.read_csv(csv)
        if idx == 0:
            positive_df = single_data_frame
        else:
            positive_df = pd.concat(
                [positive_df, single_data_frame], ignore_index=True)
        idx += 1

    negative_df_len = len(negative_df)
    positive_df = positive_df.sample(frac=1)[0:negative_df_len * 4]
    total_df = pd.concat([positive_df, negative_df], ignore_index=True)

    total_df = total_df.sample(frac=1)
    n = len(total_df)
    train, val = total_df[int(n/8):n], total_df[0:int(n/8)]
    print('train: {0}, val: {1}, rate: {2}.'.format(
        len(train), len(val), len(train) / len(val)))
    train.to_csv('train_save_d1_train.csv', index=0)
    val.to_csv('train_save_d1_val.csv', index=0)


to_csv()

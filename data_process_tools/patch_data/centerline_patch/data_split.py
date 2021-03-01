import pandas as pd

size = 1


def get_csv_path(data_dir):
    files = []
    for i in range(size):
        f = '{0}d{1}_patch_info_500.csv'.format(data_dir, i)
        files.append(f)
    return files


def to_csv():
    no_offset = get_csv_path(data_dir='no_offset/point_500_gp_1/')
    offset = get_csv_path(data_dir='offset/point_500_gp_1/')
    all_csv = no_offset + offset
    print('all_csv: ', all_csv)
    df = pd.DataFrame()
    idx = 0
    for csv in all_csv:
        single_data_frame = pd.read_csv(csv)
        if idx == 0:
            df = single_data_frame
        else:
            df = pd.concat([df, single_data_frame], ignore_index=True)
        idx += 1
    # 随机打乱数据
    df = df.sample(frac=1)
    n = len(df)
    df = df[0:int(n//512)]
    n = len(df)
    print('n={0}'.format(n))
    train, val = df[int(n/8):n], df[0:int(n/8)]
    print('train: {0}, val: {1}, rate: {2}.'.format(
        len(train), len(val), len(train) / len(val)))
    train.to_csv('train_save_d1_train.csv', index=0)
    val.to_csv('train_save_d1_val.csv', index=0)


to_csv()

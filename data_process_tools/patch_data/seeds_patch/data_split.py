import pandas as pd

size = 8


def get_csv_path(data_dir):
    files = []
    for i in range(size):
        f = '{0}d{1}_patch_info.csv'.format(data_dir, i)
        files.append(f)
    return files


def to_csv():
    negative = get_csv_path(data_dir='negative/gp_19/')
    positive = get_csv_path(data_dir='positive/gp_100/')
    all_csv = negative + positive
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
    train, val = df[int(n/8):n], df[0:int(n/8)]
    train.to_csv('train_save_d1_train.csv', index=0)
    val.to_csv('train_save_d1_val.csv', index=0)


to_csv()

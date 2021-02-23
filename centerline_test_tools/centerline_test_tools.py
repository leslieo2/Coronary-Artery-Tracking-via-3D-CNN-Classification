
from data_provider_argu import DataGenerater
from torch.utils.data import DataLoader
import torch
from centerline_net import CenterlineNet
import matplotlib.pyplot as plt


def get_dataset(save_num=0):
    '''
    :return: test set
    '''
    train_data_info_path = "train_save_d" + \
        str(save_num)+"_test.csv.keep"
    train_pre_fix_path = "../data_process_tools/patch_data/"
    train_flag = 'train'
    train_transforms = None
    target_transform = None
    test_dataset = DataGenerater(
        train_data_info_path, train_pre_fix_path, 500, train_transforms, train_flag, target_transform)

    return test_dataset


def restore_net():
    centerline_net = torch.load(
        '../checkpoint/classification_checkpoints/centerline_net_model_s1.pkl')
    return centerline_net


test_data = get_dataset(save_num=1)
test_loader = DataLoader(
    test_data, batch_size=64, shuffle=False, num_workers=16)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu")

model = restore_net()
max_points = 500
count = 0
for idx, (inputs, labels, r) in enumerate(test_loader):
    count += 1
    if count > 1:
        break
    print('inputs: ', inputs.size())
    print('labels: ', labels)
    inputs, labels, r = inputs.to(device), labels.to(
        device), r.to(device)
    outputs = model(inputs)
    outputs = outputs.view((len(labels), max_points+1))
    outputs_1 = outputs[:, :len(outputs[0])-1]  # 方向分类器
    outputs_2 = outputs[:, -1]  # 半径回归器
    print('outpouts_1: ', outputs_1)
    print('outpouts_2: ', outputs_2)

print('count=', count)

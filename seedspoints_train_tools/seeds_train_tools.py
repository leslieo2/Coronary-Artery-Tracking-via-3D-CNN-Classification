import torch
from seeds_trainner import Trainer
from seeds_net_data_provider_aug import DataGenerater
import sys
sys.path.append('..')
from models.seedspoints_net import SeedspointsNet


def get_dataset(save_num=0):
    # Replace these paths to the path where you store the data
    train_data_info_path = "../data_process_tools/patch_data/seeds_patch/train_save_d" + \
        str(save_num)+"_train.csv"
    train_pre_fix_path = "../data_process_tools/patch_data/"
    train_flag = 'train'
    train_transforms = None
    target_transform = None
    train_dataset = DataGenerater(
        train_data_info_path, train_pre_fix_path, train_transforms, train_flag, target_transform)

    val_data_info_path = "../data_process_tools/patch_data/seeds_patch/train_save_d" + \
        str(save_num)+"_val.csv"
    val_pre_fix_path = "../data_process_tools/patch_data/"
    val_flag = 'val'
    test_valid_transforms = None
    target_transform = None
    val_dataset = DataGenerater(
        val_data_info_path, val_pre_fix_path, test_valid_transforms, val_flag, target_transform)

    return train_dataset, val_dataset


if __name__ == '__main__':

    # Here we use 8 fold cross validation, save_num means to use dataset0x as the validation set
    save_num = 1
    train_dataset, val_dataset = get_dataset(save_num)
    curr_model_name = "seedspoints_net"
    model = SeedspointsNet()

    batch_size = 64
    num_workers = 16

    criterion = torch.nn.MSELoss()
    inital_lr = 0.001

    optimizer = torch.optim.Adam(filter(
        lambda p: p.requires_grad, model.parameters()), lr=inital_lr, weight_decay=0.001)

    trainer = Trainer(batch_size,
                      num_workers,
                      train_dataset,
                      val_dataset,
                      model,
                      curr_model_name,
                      optimizer,
                      criterion,
                      start_epoch=0,
                      max_epoch=100,
                      save_num=save_num,
                      initial_lr=inital_lr)

    trainer.run_train()

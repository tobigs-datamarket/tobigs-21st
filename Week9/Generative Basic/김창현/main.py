from train import train_model
from model import VAE

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import copy
from tqdm import tqdm
import wandb



def main():

    wandb.init(
    # set the wandb project where this run will be logged
    project = "VAE",
    )
    model = VAE(28*28,32,32)
    optimizer = optim.Adam(model.parameters(), lr = 0.001)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    best_model = train_model(model,optimizer,device,batch_size = 64,num_epochs=3)

    torch.save(best_model.state_dict(), f'weights/model_1st.pth')


if __name__ =='__main__':
    main()
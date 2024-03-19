#%% 

import os
import numpy as np
import random
import itertools

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from torchvision import datasets,transforms
from torchvision.utils import save_image

image_path = './images'
os.makedirs(image_path, exist_ok=True) 


#%%

class MNIST_Dataloader:
    def __init__(self, batch_size=64):
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

        self.train_data = datasets.MNIST(root='./data/', train=True, transform=transform, download=True)
        self.test_data = datasets.MNIST(root='./data/', train=False, transform=transform, download=True)

        self.train_loader = DataLoader(
            self.train_data,
            batch_size=batch_size,
            shuffle=True
        )

        self.test_loader = DataLoader(
            self.test_data,
            batch_size=batch_size,
            shuffle=False
        )

    def get_loader(self):
        return self.train_loader, self.test_loader
    

# %%


#%% 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import copy
from tqdm import tqdm
import wandb

#%%
import numpy as np
from dataset import MNIST_Dataloader
import torch
import torch.nn as nn
import time
import torch.optim as optim

def VAELoss(pred,label,mu,log_sigma2):
    recon = nn.BCELoss(reduction = 'sum')(pred, label)
    kl = 0.5*torch.sum(mu**2 + torch.exp(log_sigma2) - log_sigma2 -1)

    return recon + kl    

    

def train_model(model, optimizer, device, batch_size, num_epochs = 15):
    mnist_loader = MNIST_Dataloader(batch_size= batch_size)
    train_loader, test_loader = mnist_loader.get_loader()

    patience_check = 0
    for epoch in range(num_epochs):
        
        model.train()  # model training mode
        running_loss = 0.0
        train_loss = []
            
        start_time = time.time()  # 에폭 시작 시간 기록

        for i, data in enumerate(train_loader, 0):
            images, labels = data
            images = images.view(-1,28**2 ).to(device)
            

            print(f'Epoch : {epoch + 1}, {i}th batch train start!')
            
            mu, log_sigma2, pred = model(images)

            t_loss = VAELoss(pred, images, mu, log_sigma2)

            optimizer.zero_grad()
            
             
            t_loss.backward()
            optimizer.step()
            running_loss += t_loss.item()
            # second real update with backward
            
            train_loss.append(running_loss)
            
            _train_loss = np.mean(train_loss)

        end_time = time.time()
        total_time = end_time - start_time


        model.eval()
        with torch.no_grad():
            valid_loss = 0
            best_loss = 1
            for batch_idx, (x, _) in enumerate(test_loader): # VAE는 label이 필요없음
                x_valid = x.view(-1, 28*28).to(device)
                mu, log_sigma2, pred = model(x_valid)
                
                v_loss = VAELoss(pred, x_valid, mu, log_sigma2)
                valid_loss += v_loss.item()

            if valid_loss > best_loss:
                patience_check +=1
                    
            if patience_check >= 5:
                break
            
            else:
                best_loss = valid_loss
                patience_check = 0
                best_model = copy.deepcopy(model)        

            print('Epoch: {} Valid_Loss: {} :'.format(epoch, valid_loss/len(test_loader.dataset)))

            wandb.log({"train_loss": _train_loss, "valid_loss": valid_loss/len(test_loader.dataset), "Time":total_time})
    return best_model

    print(f'train complete!')

    # grid = gridspec.GridSpec(3, 3)
    # plt.figure(figsize = (10, 10))
    # plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

    # for i in range(9):
    #     ax = plt.subplot(grid[i])
    #     x, y = valid[i]
    #     _, _, pred = best_model(x.view(-1,784))
    #     plt.imshow(pred.detach().numpy().reshape(28,28), cmap = 'gray_r')
    #     ax.get_xaxis().set_visible(False)
    #     ax.get_yaxis().set_visible(False)
    #     ax.set_title('label : {}'.format(y))

    # wandb.log({"pred" : ax})
    wandb.finish()
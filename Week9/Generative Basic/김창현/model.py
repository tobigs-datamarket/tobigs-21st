#%%
import torch
import torch.nn as nn
import torch.nn.functional as F


class Encoder(nn.Module):
    def __init__(self, x_dim , h_dim, z_dim):


        super(Encoder,self).__init__()

        self.fc1 = nn.Sequential(
            nn.Linear(x_dim,h_dim),
            nn.ReLU(),
            nn.Dropout(p=0.2)
            
        )

        self.fc2 = nn.Sequential(
            nn.Linear(h_dim, h_dim),
            nn.ReLU(),
            nn.Dropout(p=0.2)
        )

        self.mu = nn.Linear(h_dim, z_dim)
        self.logvar = nn.Linear(h_dim,z_dim)

    def reparameterization(self, mu, logvar):
        std = torch.exp(logvar / 2)
        eps = torch.randn_like(std)
        return mu + eps * std
    ## 역전파 학습을 위한 도구

    def forward(self,x):
        x = self.fc2(self.fc1(x))

        mu = F.relu(self.mu(x))
        logvar = F.relu(self.logvar(x))

        z = self.reparameterization(mu, logvar)
        return z, mu, logvar
# %%
    
## Linear한 층
class Decoder(nn.Module):
    def __init__(self, x_dim, h_dim, z_dim):
        super(Decoder, self).__init__()

        # 1st hidden layer
        self.fc1 = nn.Sequential(
            nn.Linear(z_dim, h_dim),
            nn.ReLU(),
            nn.Dropout(p=0.2),
        )

        # 2nd hidden layer
        self.fc2 = nn.Sequential(
            nn.Linear(h_dim, h_dim),
            nn.ReLU(),
            nn.Dropout(p=0.2)
        )

        # output layer
        self.fc3 = nn.Linear(h_dim, x_dim)

    def forward(self, z):
        z = self.fc2(self.fc1(z))
        x_reconst = F.sigmoid(self.fc3(z))
        return x_reconst
    
#%% 

class VAE(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(VAE, self).__init__()

        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.latent_dim = latent_dim

        self.encoder = Encoder(self.input_dim, self.hidden_dim, self.latent_dim)
        self.decoder = Decoder(self.input_dim, self.hidden_dim, self.latent_dim) # symmetric 



    def forward(self, x):
        '''recognition model : q(z|x)'''

        z, mu, log_sigma2 = self.encoder(x)


        '''generative mode   l : p(x|z)'''
        pred = self.decoder(z)

        return mu, log_sigma2, pred
      

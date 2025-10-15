import torch
import torch.nn as nn
import torch.nn.functional as F

class LayerNormalization(nn.Module):
    def __init__(self, feature, eps=1e-6):
        super().__init__()
        self.w=nn.Parameter(torch.ones(feature))
        self.b=nn.Parameter(torch.zeros(feature))
        self.eps=eps

    def forward(self,x):
        mean=x.mean(-1,keepdim=True)
        std=x.std(-1,keepdim=True)
        return self.w*(x-mean)/(std+self.eps)+self.b


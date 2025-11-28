import torch
import torch.nn as nn
import math
import numpy as np


class AbsolutePositionEmbedding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        self.d_model=d_model

        self.pe=torch.zeros(max_len, d_model)
        self.position=torch.arange(0, max_len).unsqueeze(1).float()

        div_term=torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000)/d_model))

        self.pe[:][0::2]=torch.sin(self.position*div_term)
        self.pe[:][1::2]=torch.cos(self.position*div_term)

        self.register_buffer('pe', self.pe.unsqueeze(-1))
    
    def forward(self, x):
        seq_len=x.size(1)
        return x+self.pe[:,seq_len]

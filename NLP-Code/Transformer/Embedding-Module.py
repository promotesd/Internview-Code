import numpy 
import torch
import torch.nn as nn
import math
from typing import Dict
from einops import rearrange
from jaxtyping import Int, Float


class Embedding(nn.Module):
    def __init__(self, num_embeddings:int, embedding_dim:int, device:torch.device|None=None, dtype:torch.dtype|None=None):
        super().__init__()
        factory_kwargs:Dict[str, torch.device | torch.dtype]={}
        if device is not None:
            factory_kwargs['device']=device
        if dtype is not None:
            factory_kwargs['dtype']=dtype

        self.weight=nn.Parameter(torch.empty((num_embeddings,embedding_dim),dtype=dtype,device=device),requires_grad=True)
        nn.init.trunc_normal_(self.weight, mean=0, std=1, a=-3, b=3)

    def forward(self,token_ids:Int[torch.Tensor,'...'])->Float[torch.Tensor,'... d_model']:
        return self.weight[token_ids]



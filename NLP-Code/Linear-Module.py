import numpy
import math
import torch
import torch.nn as nn



class Linear(nn.Module):
    
    def __init__(self, in_features:int, out_features:int, device:torch.device|None=None, dtype:torch.dtype|None=None):
        super().__init__()
        self.in_features=in_features
        self.out_features=out_features
        factory_kwargs: dict[str, torch.device|torch.dtype]={}
        if device is not None:
            factory_kwargs["device"]=device
        if dtype is not None:
            factory_kwargs["dtype"]=dtype

        self.weight=nn.Parameter(torch.empty((self.out_features, self.in_features),**factory_kwargs))

        std=math.sqrt(2/(in_features+out_features))
        nn.init.trunc_normal_(tensor=self.weight,mean=0,std=std,a=-3*std,b=3*std)

    def forward(self,x:torch.Tensor)->torch.Tensor:
        return torch.matmul(x,self.weight.T)
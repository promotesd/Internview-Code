import torch
import torch.nn as nn
import torch.nn.functional as F

class RMSNorm(nn.Module):
    def __init__(self, dim:int , eps=1e-6):
        super().__init__()
        self.w=nn.Parameter(torch.ones(dim))
        self.eps=eps

    def _norm(self, x):
        return x*torch.rsqrt(x.pow(2).mean(-1,keepdim=True)+self.eps)
    
    def forward(self,x):
        output=self._norm(x.float()).type_as(x)
        return output*self.w
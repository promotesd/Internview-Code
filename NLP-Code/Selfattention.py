import torch
import math
import torch.nn as nn
import numpy as np

class MHA(nn.Module):
    def __init__( self, num_head, dimension_v, dimension_k, d_k, d_v, d_o):
        super.__init__()
        self.num_head=num_head
        self.dimension_v=dimension_v
        self.dimension_k=dimension_k
        self.fc_k=nn.Linear(dimension_k, num_head*d_k, False)
        self.fc_q=nn.Linear(dimension_k, num_head*d_k, False)
        self.fc_v=nn.Linear(dimension_v, num_head*d_v, False)
        self.fc_o=nn.Linear(num_head*d_v, d_o)
        self.softmax=nn.Softmax(dim=2)

    def forward(self, q, k, v, mask):
        batch, n_q, dimension_q=q.size()
        batch, n_k, dimension_k=k.size()
        batch, n_v, dimension_v=v.size()

        q=self.fc_q(q)
        k=self.fc_k(k)
        v=self.fc_v(v)

        q=q.view(batch, n_q, self.num_head, self.d_q).permute(2, 0, 1, 3).contiguous().view(-1, n_q, self.d_q)
        k=k.view(batch, n_k, self.num_head, self.d_k).permute(2, 0, 1, 3).contiguous().view(-1, n_k, self.d_k)
        v=v.view(batch, n_v, self.num_head, self.d_v).permute(2, 0, 1, 3).contiguous().view(-1, n_v, self.d_v)

        attention=torch.matmul(q, k.transpose(-2,-1))/math.sqrt(self.d_k)
        mask=mask.repeat(self.num_head,1,1)
        attention=attention+mask
        attention=self.softmax(attention)

        output=torch.matmul(attention, v)
        output=output.view(self.num_head, batch, n_q, self.d_v).permute(1,2,0,3).contiguous().view(batch, n_q, -1)
        output=self.fc_o(output)
        return attention, output
    

        
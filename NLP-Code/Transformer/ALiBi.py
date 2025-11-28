import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class ALiBiMultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        assert embed_dim%num_heads==0, "embed dimension should be divisivle by num_heads"
        self.embed_dim=embed_dim
        self.num_heads=num_heads
        self.head_dim=embed_dim//num_heads
        self.qkv=nn.Linear(embed_dim, embed_dim*3)
        slopes=torch.pow(2, 8*torch.arange(0, -num_heads, -1,dtype=torch.float32)/num_heads)
        self.register_buffer("slopes", slopes.view(num_heads,1,1))
        
        self.out_proj=nn.Linear(embed_dim,embed_dim)

    def _create_bias_matrix(self, seq_len):
        #生成位置索引
        positions=torch.arange(seq_len, device=self.slopes.device)
        #计算相对位置
        rel_positions=torch.abs(positions.unsqueeze(0)-positions.unsqueeze(1))
        #乘上斜率
        bias=-self.slopes*rel_positions
        return bias
    
    def forward(self,x):
        batch_size, seq_len, _=x.shape
        qkv=self.qkv(x)
        qkv=qkv.reshape(batch_size, seq_len, 3, self.num_heads, self.head_dim)
        qkv=qkv.permute(2,0,3,1,4).contiguous() #(3, batch_size,self.num_heads, seq_len , self.embed_dim)
        q,k,v=qkv[0],qkv[1],qkv[2]
        attn_score=torch.matmul(q,k.transpose(-2,-1))/math.sqrt(self.head_dim)
        bias=self._create_bias_matrix(seq_len)
        attn_score=attn_score+bias
        attn_prob=F.softmax(attn_score, -1)
        attn_output=torch.matmul(attn_prob,v)
        attn_output=attn_output.permute(0,2,1,3).contiguous().reshape(batch_size, seq_len, self.embed_dim)

        #输出投影
        return self.out_proj(attn_output)
    

# 测试实现
if __name__ == "__main__":
    # 创建随机输入 (batch=2, seq_len=10, embed_dim=64)
    x = torch.randn(2, 10, 64)
    # 初始化ALiBi注意力层 (8个头)
    alibi_attn = ALiBiMultiHeadAttention(embed_dim=64, num_heads=8)
    # 前向传播
    output = alibi_attn(x)
    print(f"输入形状: {x.shape}")
    print(f"输出形状: {output.shape}")
    print(f"ALiBi偏置矩阵示例（头1，序列长度10）:\n{alibi_attn._create_bias_matrix(10)[0]}")





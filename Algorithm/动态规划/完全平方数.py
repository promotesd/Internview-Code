from functools import cache
from math import isqrt
from math import inf

@cache
def dfs(i,j):
    if i==0:
        return inf if j else 0
    if j<i*i:
        return dfs(i-1,j)
    return min(dfs(i-1,j),dfs(i,j-i*i)+1)


class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n),n)
        
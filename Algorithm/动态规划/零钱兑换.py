from typing import List
from functools import cache
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i,j):
            if i<0:
                return 0 if j==0 else inf
            if coins[i]>j:
                return dfs(i-1,j)
            return min(dfs(i-1,j),dfs(i, j-coins[i])+1)
        ans=dfs(len(coins)-1, amount)
        return ans if ans<inf else -1
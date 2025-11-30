from typing import List
from functools import cache
from math import inf

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i<0 or j<0:
                return inf
            if i==0 and j==0:
                return grid[0][0]
            return min(dfs(i-1,j)+grid[i][j], dfs(i,j-1)+grid[i][j])
        return dfs(len(grid)-1, len(grid[0])-1)
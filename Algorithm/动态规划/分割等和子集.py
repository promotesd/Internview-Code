from typing import List
from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i:int, j:int):
            if i<0:
                return j==0
            if nums[i]>j:
                return dfs(i-1,j)
            return dfs(i-1,j) or dfs(i-1, j-nums[i])
        
        s=sum(nums)
        return s%2==0 and dfs(len(nums)-1, s//2)
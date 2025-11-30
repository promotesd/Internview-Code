from typing import List
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i:int)->int:
            res=0
            for j in range(i):
                if nums[j]<nums[i]:
                    res=max(res, dfs(j))
            return res+1
        return max(dfs(i) for i in range(len(nums)))

            

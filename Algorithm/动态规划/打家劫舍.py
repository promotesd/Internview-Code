from typing import List
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-1),dfs(i-2)+nums[i])
        return dfs(len(nums)-1)
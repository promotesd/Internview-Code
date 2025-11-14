from typing import List
from math import inf


##贪心+枚举右，维护左
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        ans=0
        pre_min=inf
        for x in nums:
            ans=max(ans, x-pre_min)
            ##去除0这一步，通过将pre_min传入并且取最小
            pre_min=min(x, pre_min)
        return ans if ans>0 else -1

from typing import List
from math import inf

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        suf_max=[0]*(n+1)
        ans=-inf
        pre_max=-inf
        for i in range(n-1, 1, -1):
            suf_max[i]=max(suf_max[i+1], nums[i])
        for index, num in enumerate(nums):
            ans=max(ans, (pre_max-num)*suf_max[index+1])
            pre_max=max(pre_max, num)
        return ans if ans>0 else 0
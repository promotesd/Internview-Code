from typing import List
from math import inf

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n=len(nums)
        suf=[0]*n
        suf[-1]=nums[-1]
        for i in range(n-2, 1, -1):
            suf[i]=min(suf[i+1], nums[i])
        ans=inf
        pre=nums[0]
        for i in range(1,n-1):
            if pre<nums[i]>suf[i+1]:
                ans=min(ans, pre+nums[i]+suf[i+1])
            pre=min(pre, nums[i])
        return ans if ans<inf else -1
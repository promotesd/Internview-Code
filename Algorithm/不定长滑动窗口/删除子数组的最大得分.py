from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left= ans= maxval=0
        cnt=defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num]+=1
            maxval+=num
            while cnt[num]>1:
                cnt[nums[left]]-=1
                maxval-=nums[left]
                left+=1
            ans=max(ans, maxval)
        return ans
from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=left=0
        cnt=defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num]+=1
            while cnt[num]>k:
                cnt[nums[left]]-=1
                left+=1
            ans=max(ans, right-left+1)
        return ans
        
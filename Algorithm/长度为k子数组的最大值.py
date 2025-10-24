from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        s=0
        cnt=defaultdict(int)
        for i, x in enumerate(nums):
            s+=x
            cnt[x]+=1

            if i-k+1<0:
                continue

            if len(cnt)==k:
                ans=max(ans,s)
            
            s-=nums[i-k+1]
            cnt[nums[i-k+1]]-=1
            if cnt[nums[i-k+1]]==0:
                del cnt[nums[i-k+1]]
        return ans
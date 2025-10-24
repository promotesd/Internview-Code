from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        s=0
        avgs=[-1]*len(nums)
        for idx, x in enumerate(nums):
            s+=x
            if idx<2*k:
                continue
            avgs[idx-k]=s//(2*k+1)
            s-=nums[idx-2*k]
        return avgs
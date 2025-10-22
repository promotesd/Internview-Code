from typing import List
from math import inf

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg=-inf
        s=0
        for i, num in enumerate(nums):

            s+=num

            if i-k+1<0:
                continue

            max_avg=max(max_avg, s)

            s-=nums[i-k+1]
        return max_avg/k
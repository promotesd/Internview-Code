from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        f_min=[0]*n
        f_max=[0]*n
        f_min[0]=f_max[0]=nums[0]
        for i in range(1,n):
            x=nums[i]
            f_max[i]=max(f_max[i-1]*x, f_min[i-1]*x, x)
            f_min[i]=min(f_min[i-1]*x, f_max[i-1]*x, x)
        return max(f_max)
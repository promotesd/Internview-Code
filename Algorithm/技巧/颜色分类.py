from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0=p1=0
        for i, x in enumerate(nums):
            nums[i]=2
            if x<=1:
                nums[p1]=1
                p1+=1
            if x==0:
                nums[p0]=0
                p0+=1
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        idx=0
        for x in nums:
            if x:
                nums[idx]=x
                idx+=1

        nums[idx:]=[0]*(n-idx)
        return nums
        
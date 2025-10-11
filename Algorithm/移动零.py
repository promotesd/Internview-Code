from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        stack_size=0
        for x in nums:
            if x:
                nums[stack_size]=x
                stack_size+=1
        nums[stack_size:]=0*(len(nums)-stack_size)
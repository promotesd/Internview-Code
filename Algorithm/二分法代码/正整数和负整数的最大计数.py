from typing import List

class Solution:

    def lowerbound(self, nums:List[int], target:int):
        left, right =0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        return left


    def maximumCount(self, nums: List[int]) -> int:
        pos=len(nums)-self.lowerbound(nums, 0)
        neg=self.lowerbound(nums, -1)
        return pos if neg<pos else neg
        


        
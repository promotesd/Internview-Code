from typing import List


class Solution:

    def lower_bound(self, nums:List[int], target):
        left, right=0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lower_bound(nums, target)
        
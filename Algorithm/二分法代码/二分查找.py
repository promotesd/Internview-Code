from typing import List

class Solution:

    def lower_bound(self, nums:List[int], target: int):
        left, right= 0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return left

    def search(self, nums: List[int], target: int) -> int:

        pos=self.lower_bound(nums, target)

        if pos==len(nums) or nums[pos]!=target:
            return -1
        else:
            return pos
        
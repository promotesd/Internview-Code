from typing import List

class Solution:
    def lowerbound(self, nums:List[int], target:int)->int:
        left, right=0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1

        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos=[]
        pos.append(self.lowerbound(nums, target-1))
        pos.append(self.lowerbound(nums, target)-1)
        return pos if pos[0]<=pos[1] else [-1,-1]

        
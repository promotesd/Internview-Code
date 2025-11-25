from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)

        while left+1<right:
            mid=left+(right-left)//2
            x=nums[mid]
            if target>nums[-1]>=x:
                right=mid
            elif x > nums[-1] >= target:
                left=mid
            elif target<=x:
                right=mid
            else:
                left=mid
        return right if right<len(nums) and nums[right]==target else -1
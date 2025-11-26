from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx=0
        for i, jump in enumerate(nums):
            if i>mx:
                return False
            mx=max(mx, i+jump)
        return True
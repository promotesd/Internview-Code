from math import inf
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=-inf
        left=0
        n=len(height)
        right=n-1
        while left<right:
            if height[left]<height[right]:
                ans=max(ans, height[left]*(right-left))
                left+=1
            elif height[right]<=height[left]:
                ans=max(ans, height[right]*(right-left))
                right-=1
        return ans

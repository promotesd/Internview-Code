from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        ans=0
        for num in num_set:
            if num-1 in num_set:
                continue
            y=num+1
            while y in num_set:
                y+=1
            ans=max(ans, y-num)
        return ans
            
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res=target-nums[i]
            if res in nums[i+1:]:
                return [i,nums[i+1:].index(res)+i+1]
            
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        hashtable=dict()
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]]=i
        return []

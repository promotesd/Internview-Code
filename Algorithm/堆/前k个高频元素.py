from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        fremax=max(cnt.values())
        bucket=[[] for _ in range(len(nums)+1)]
        for num, c in cnt.items():
            bucket[c].append(num)
        ans=[]
        for i in reversed(bucket):
            ans+=i
            if len(ans)==k:
                return ans
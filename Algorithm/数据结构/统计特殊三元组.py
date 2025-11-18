from collections import Counter, defaultdict
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n=len(nums)
        suf=Counter(nums)
        prev=defaultdict(int)
        ans=0
        for x in nums:
            suf[x]-=1
            ans+=suf[x*2]*prev[x*2]
            prev[x]+=1
        return ans%MOD
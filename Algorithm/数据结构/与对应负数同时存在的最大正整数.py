from typing import List

class Solution:
    def findMaxK(self, nums:List[int])->int:
        ans=-1
        s=set()
        for n in nums:
            if -n in s:
                ans=max(ans,abs(n))
            s.add(n)
        return ans


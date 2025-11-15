from typing import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD=1_000_000_007
        ans=s=0
        cnt=Counter(point[1] for point in points)
        for c in cnt.values():
            line=c*(c-1)//2
            ans+=s*line
            s+=line
        return ans%MOD

from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashtable=defaultdict(int)
        ans=0
        for domino in dominoes:
            if tuple(sorted(domino)) in hashtable:
                ans+=hashtable[tuple(sorted(domino))]
            hashtable[tuple(sorted(domino))]+=1
        return ans

from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums:List[int])->int:
        ans=0
        cnt=defaultdict(int)
        for n in nums:
        ##这里不能将cnt[n]+=1放在ans+=cnt[n]前面，会出现i=j的情况
            if n in cnt:
                ans+=cnt[n]
            cnt[n]+=1

        return ans
from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits:List[int])->int:
        left, ans=0
        cnt=defaultdict(int)
        for right, fruit in enumerate(fruits):
            cnt[fruit]+=1
            while len(cnt)>2:
                out=fruits[left]
                cnt[out]-=1
                if cnt[out]==0:
                    del cnt[out]
                left+=1
            ans=max(ans, right-left+1)
        return ans

        
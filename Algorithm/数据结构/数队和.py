from typing import List
from collections import defaultdict

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        cnt=defaultdict(int)

        for index, num in enumerate(nums):
            if target-num in cnt and cnt[target-num]:
                ans.append([target-num,num])
                cnt[target-num]-=1
            else:
                cnt[num]+=1

        return ans
        
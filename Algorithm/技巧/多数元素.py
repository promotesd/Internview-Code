from typing import List
from math import ceil
from collections import defaultdict

class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        ans=hp=0

        for num in nums:
            if hp==0:
                ans, hp = num, 1
            else:
                hp+=1 if ans==num else -1
        return ans

    def majorityElement_dict(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        ans=0
        for num in nums:
            cnt[num]+=1
        for k,v in cnt.items():
            if v>=ceil(len(nums)/2):
                ans=k
        return ans

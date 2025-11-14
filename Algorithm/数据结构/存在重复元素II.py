from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag=False
        cnt=defaultdict(int)
        for index, x in enumerate(nums):
            
            if x in cnt and index-cnt[x]<=k:
                flag=True

            cnt[x]=index
        return flag


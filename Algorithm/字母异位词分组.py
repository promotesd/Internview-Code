from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for str in strs:
            sort_str=''.join(sorted(str))
            d[sort_str].append(str)
        return list(d.values)
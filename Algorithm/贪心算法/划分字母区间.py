from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={c:i for i, c in enumerate(s)}
        ans=[]
        start, end = 0, 0
        for i, c in enumerate(s):
            end=max(end, last[c])
            if end==i:
                ans.append(end-start+1)
                start=i+1

        return ans

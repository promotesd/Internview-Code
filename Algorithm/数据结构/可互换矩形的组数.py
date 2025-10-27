from typing import List
from collections import defaultdict

class solution:
    def interchangeableRectangles(self, rectangles:List[List[int]])->int:
        cnt=defaultdict(float)
        ans=0
        for rectangle in rectangles:
            ratio=rectangle[0]/rectangle[1]
            if ratio in cnt:
                ans+=cnt[ratio]
            cnt[ratio]+=1
        return ans


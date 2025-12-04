from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        right=[n]*n
        st=[]
        for i, h in enumerate(heights):
            while st and heights[st[-1]]>=h:
                right[st.pop()]=i
            if st:
                left[i]=st[-1]
            st.append(i)

        ans=0
        for h, l, r in zip(heights, left, right):
            ans=max(ans, h*(r-l-1))
        return ans
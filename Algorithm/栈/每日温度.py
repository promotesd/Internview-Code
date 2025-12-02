from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[]
        for idx, num in enumerate(temperatures):
            while st and num>temperatures[st[-1]]:
                ans[st[-1]]=idx-st[-1]
                st.pop()
            st.append(idx)
        return ans
            
from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        n=len(s)
        suf=Counter(s[1:])
        prev=set()
        st = set()
        for i in range(1, n-1):
            mid=s[i]
            suf[mid]-=1
            if suf[mid]==0:
                del suf[mid]
            prev.add(s[i-1])
            for alpha in suf.keys()&prev:
                ans+=1
                st.add(alpha + mid)
        return len(st)
            

            
        
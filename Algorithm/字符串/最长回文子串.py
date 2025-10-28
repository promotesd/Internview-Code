class Solution:
    def longestPalindrome(self, s:str)->str:
        n=len(s)
        ans_left=ans_right=0
        for i in range(2*n-1):
            l,r=i//2, (i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if ans_right-ans_left<r-l:
                ans_left, ans_right=l+1,r
        return s[ans_left: ans_right]
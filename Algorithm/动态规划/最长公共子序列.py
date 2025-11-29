from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)

        @cache

        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return dfs(i-1,j-1)+1
            else:
                return max(dfs(i,j-1), dfs(i-1, j))
        return dfs(m-1,n-1)
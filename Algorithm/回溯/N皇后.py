from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        col=[0]*n

        def is_valid(r,c):
            for R in range(r):
                C=col[R]
                if C+R==c+r or R-C==r-c:
                    return False
            return True

        def dfs(r, s):
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in col])
                return 

            for c in s:
                if is_valid(r,c):
                    col[r]=c
                    dfs(r+1,s-{c})
        dfs(0,set(range(n)))
        return ans


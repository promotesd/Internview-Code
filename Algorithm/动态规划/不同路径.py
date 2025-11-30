from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dfs(i:int,j:int)->int:
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            return dfs(i-1,j)+dfs(i, j-1)
        return dfs(m-1, n-1)

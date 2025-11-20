MAP=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)

        if n==0:
            return []

        path=['']*n
        ans=[]

        def dfs(i):
            if i==n:
                ans.append(''.join(path))
                return
            for c in MAP[int(digits[i])]:
                path[i]=c
                dfs(i+1)
        dfs(0)
        return ans
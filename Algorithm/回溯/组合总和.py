from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        path=[]
        ans=[]

        def dfs(i, left):
            if left==0:
                ans.append(path.copy())
                return 
            if left<0 or i==len(candidates):
                return

            dfs(i+1, left)
            path.append(candidates[i])
            dfs(i,left-candidates[i])
            path.pop()
        dfs(0, target)
        return ans

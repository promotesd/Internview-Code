from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        path=['']*n
        def dfs(i, s):
            if i==n:
                ans.append(path.copy())
                return 
            for x in s:
                path[i]=x
                dfs(i+1,s-{x})
        dfs(0,set(nums))
        return 
    
    def permute_arrmark(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        path=['']*n
        on_path=[False]*n

        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return

            for j in range(n):
                if not on_path[j]: 
                    path[i]=nums[j]
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False
        dfs(0)

        return ans
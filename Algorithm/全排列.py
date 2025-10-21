from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, used, path, res):
            if size==depth:
                res.append(path[:])
                return 
            
            for i in range(size):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])

                    dfs(nums, size, depth+1, used, path, res)

                    used[i]=False
                    path.pop()
        
        size=len(nums)
        if len(nums)==0:
            return []

        used=[False for _ in range(size)]
        res=[]
        dfs(nums, size, 0, used, [], res)
        return res
        
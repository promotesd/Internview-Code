from typing import List

class Solution:
    def subsets(self, nums:List[int])->List[List[int]]:
        n
        path=[]
        ans=[]
        def dfs(i:int):
            if 
from typing import List

class Solution:
    def subsets(self, nums:List[int])->List[List[int]]:
        path=[]
        ans=[]
        def dfs(i:int):
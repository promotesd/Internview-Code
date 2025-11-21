from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        path=['']*2*n
        ans=[]
        
        def dfs(left, right):
            if right==n:
                ans.append(''.join(path))
                return 
            
            if left<n:
                path[left+right]='('
                dfs(left+1,right)
            if right<left:
                path[left+right]=')'
                dfs(left,right+1)
        dfs(0,0)
        return ans
        
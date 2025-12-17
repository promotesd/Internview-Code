from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -1
            l_len=dfs(node.left)
            r_len=dfs(node.right)
            nonlocal ans
            ans=max(ans, l_len+r_len+2)
            return max(l_len, r_len)+1
        dfs(root)
        return ans

        
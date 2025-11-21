from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        cnt=Counter(c for row in board for c in row)
        if cnt<Counter(word):
            return False
        if cnt[word[-1]]<cnt[word[0]]:
            word=word[::-1]

        m,n=len(board), len(board[0])
        def dfs(i, j, k):
            if board[i][j]!=word[k]:
                return False

            if k==len(word)-1:
                return True
            
            board[i][j]=''
            for x,y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if 0<=x<m and 0<=y<n and dfs(x,y,k+1):
                    return True
            board[i][j]= word[k]
            return False
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
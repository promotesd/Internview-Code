class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=k
        action=0
        for idx, c in enumerate(blocks):
            if c=='W':
                action+=1
            
            if idx<k-1:
                continue

            ans=min(ans,action)

            if blocks[idx-k+1]=='W':
                action-=1
        return ans


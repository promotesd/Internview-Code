class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        ans=0
        for i, c in enumerate(s):
            if c=='(':
                stk.append(i)
            elif len(stk)>1:
                stk.pop()
                ans=max(ans, i-stk[-1])
            else:
                stk[0]=i

        return ans
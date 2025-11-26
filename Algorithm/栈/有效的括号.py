class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        MAP={')':'(', ']':'[','}':'{'}
        st=[]
        for c in s:
            if c not in MAP:
                st.append(c)
            elif not st or MAP[c]!=st.pop():
                return False
        return not st
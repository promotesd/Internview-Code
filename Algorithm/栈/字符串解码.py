class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        def decode():
            nonlocal i
            res=''
            k=0
            while i<len(s):
                c=s[i]
                i+=1
                if c.isalpha():
                    res+=c
                elif c.isdigit():
                    k=k*10+int(c)
                elif c=='[':
                    res+=decode()*k
                    k=0
                else:
                    break
            return res
        return decode()

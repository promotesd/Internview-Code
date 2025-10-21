from typing import List

class Solution:
    def maxVowels(self, s:str, k:int)->int:
        ans = vowel = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                vowel+=1
            
            if i-k+1<0:
                continue

            ans=max(ans,vowel)

            if s[i-k+1] in "aeiou":
                vowel-=1
        
        return ans
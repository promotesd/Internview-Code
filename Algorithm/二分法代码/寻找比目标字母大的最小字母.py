from typing import List

class Solution:

    def lowerbound(self, letters:List[str], target:str)->int:
        left, right= 0, len(letters)-1
        while left<=right:
            mid=left+(right-left)//2
            if  ord(letters[mid])<=ord(target):
                left=mid+1
            else:
                right=mid-1
        return left

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start=self.lowerbound(letters, target)
        if start == len(letters):
            return letters[0]
        else:   
            return letters[start]
        
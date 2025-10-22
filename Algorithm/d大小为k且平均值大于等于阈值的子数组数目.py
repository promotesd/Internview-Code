from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        s=0
        for i,num in enumerate(arr):
            s+=num
            if i-k+1<0:
                continue

            if s/k>=threshold:
                res+=1

            s-=arr[i-k+1]
        return res

        
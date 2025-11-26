from typing import List
from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2=nums2, nums1
        m=len(nums1)
        n=len(nums2)

        nums1=[-inf]+nums1+[inf]
        nums2=[-inf]+nums2+[inf]

        i, j =0, (m+n+1)//2

        while nums1[i+1]<=nums2[j]:
            i+=1
            j-=1
        max1=max(nums1[i], nums2[j])
        min2=min(nums1[i+1],nums2[j+1])

        return max1 if (m+n)%2 else (max1+min2)/2
        
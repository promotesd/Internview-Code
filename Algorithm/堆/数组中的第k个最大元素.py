from typing import List
from random import randint

class Solution:

    def partition(self, nums:List[int], left:int, right:int):
        i=randint(left, right)
        pivot=nums[i]
        nums[i], nums[left]=nums[left], nums[i]
        i, j =left+1, right

        while True:
            while i<=j and nums[i]<pivot:
                i+=1
            while i<=j and nums[j]>pivot:
                j-=1
            if i>=j:
                break
            nums[i], nums[j]=nums[j], nums[i]
            i+=1
            j-=1
        nums[left], nums[j]=nums[j], nums[left]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target=n-k
        left=0
        right=n-1
        while True:
            j=self.partition(nums, left, right)
            if j==target:
                return nums[j]
            if j>target:
                right=j-1
            else:
                left=j+1
        
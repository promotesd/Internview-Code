from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)

        for i in range(0, n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            if nums[i]+nums[n-1]+nums[n-2]<0:
                continue
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j-1]==nums[j]:
                        j+=1
                        continue
                    k-=1
                    while j<k and nums[k+1]==nums[k]:
                        k-=1
                        continue
        return ans
                    


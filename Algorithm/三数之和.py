from typing import List

class Solution:
    def threesum(self, nums:List[int])->List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            x=nums[i]
            if i>0 and x==nums[i-1]:
                continue
            elif x+nums[i+1]+nums[i+2]>0:
                break
            elif x+nums[-2]+nums[-1]<0:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=x+nums[j]+nums[k]
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    ans.append([x,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k+1]==nums[k]:
                        k-=1
        return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]

        for i in range(len(nums)):
            j,k=i+1,len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue

            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]):
                        j+=1

                elif sum<0:
                    j+=1
                else:
                    k-=1

        return ans     
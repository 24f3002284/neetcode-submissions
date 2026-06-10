class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        ans=[]
        nums.sort()
        
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            tar=-nums[i]
            j=i+1
            k=l-1
            while(j<k):
                if(nums[j]+nums[k]==tar):
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]): j+=1
                    while(j<k and k<l-1 and nums[k]==nums[k+1]): k-=1
                    
                elif(nums[j]+nums[k]>tar):
                    k-=1
                else:
                    j+=1

            

        return ans

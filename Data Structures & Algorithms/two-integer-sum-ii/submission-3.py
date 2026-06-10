class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums=numbers
        # ans=[]
        # n=len(nums)
        
        # i=0
        # j=n-1

        # while i<n:
        #     tar=target-nums[i]
        #     while j>=0:
        #         if nums[j]==tar:
        #             ans.append(i+1)
        #             ans.append(j+1)
        #             return ans
        #         elif nums[j]>tar:
        #             j-=1
        #         else:
        #             i+=1                    

        # return [-1,-1]
        
        nums=numbers
        i,j=0,len(nums)-1

        while i<j:
            curr=nums[i]+nums[j]
            
            if(curr==target):
                return [i+1,j+1]
            elif(curr<target):
                i+=1
            else:
                j-=1

        return [-1,-1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        ans=[]
        
        for i in range(len(nums)):
            tar=target-nums[i]
            for j in range(len(nums)-1,-1,-1):
                if nums[j]==tar:
                    ans.append(i+1)
                    ans.append(j+1)
                    return ans

        return [-1,-1]
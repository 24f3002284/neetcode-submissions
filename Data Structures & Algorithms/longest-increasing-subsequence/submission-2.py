class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for i in range(n)] #0 to n-1. all no.s of nums array

        dp[n-1]=1
        #LIS if we start at the last idx=1, since no increasing subsequence of length>1 can be formed with strting idx as the last idx
        for i in range(n-1,-1,-1):
            for j in range(i+1,n,1):
                if nums[j]>nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)

                
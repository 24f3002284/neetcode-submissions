class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0,0]
        dp.extend(nums)

        for i in range(2,2+len(nums)):
            dp[i]=max(dp[i-2]+dp[i],dp[i-1])

        return dp[len(nums)+1]
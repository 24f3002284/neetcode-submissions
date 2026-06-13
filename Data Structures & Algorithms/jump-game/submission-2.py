class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*(n+1)
        dp[n-1]=True

        for idx in range(len(nums)-2,-1,-1):
            for jump in range(nums[idx]+1):
                if jump+idx<=n-1:
                    dp[idx]=dp[idx] or dp[idx+jump]
                    # if dp[idx]==True:
                    #     break

        return dp[0]
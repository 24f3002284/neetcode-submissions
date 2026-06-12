class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}

        def dfs(idx,sum):
            if (idx,sum) in dp:
                return dp[(idx,sum)]
            if idx==n and sum==target:
                return 1
            if idx==n:
                return 0

            dp[(idx,sum)]=dfs(idx+1,sum+nums[idx])+dfs(idx+1,sum-nums[idx])
            return dp[(idx,sum)]

        return dfs(0,0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        def dfs(idx,sum):
            if idx==n and sum==target:
                return 1
            if idx==n:
                return 0

            return dfs(idx+1,sum+nums[idx])+dfs(idx+1,sum-nums[idx])

        return dfs(0,0)
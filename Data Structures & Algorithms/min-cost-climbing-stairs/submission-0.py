class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        n=len(cost)

        dp[-1]=0
        dp[-2]=cost[-1]

        for i in range(n-2,-1,-1):
            dp[i]=min(cost[i]+dp[i+1],cost[i]+dp[i+2])

        return min(dp[0],dp[1]) # we r allowed to start at 0th or 1st idx
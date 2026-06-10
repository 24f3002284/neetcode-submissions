class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]


        def houseRobber1(arr):
            dp=[0,0]
            dp.extend(arr)

            for i in range(2,len(arr)+2):
                dp[i]=max(dp[i]+dp[i-2],dp[i-1])

            return dp[len(arr)+1]        
        
        return max(houseRobber1(nums[1:]),houseRobber1(nums[:-1]))
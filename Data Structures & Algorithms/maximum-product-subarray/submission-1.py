class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax,ans=1,1,float('-inf')

        for n in nums:
            tmp=curMin
            curMin=min(n,curMin*n,curMax*n)
            curMax=max(curMax*n,n,tmp*n)
            ans=max(curMin,curMax,ans)

        return ans
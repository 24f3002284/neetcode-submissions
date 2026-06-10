class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPdt=[1]*len(nums)
        rightPdt=[1]*len(nums)

        pdt=1
        for i in range(1,len(nums)):
            leftPdt[i]=leftPdt[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            rightPdt[i]=rightPdt[i+1]*nums[i+1]

        ans=[]
        for i in range(len(nums)):
            ans.append(leftPdt[i]*rightPdt[i])

        return ans
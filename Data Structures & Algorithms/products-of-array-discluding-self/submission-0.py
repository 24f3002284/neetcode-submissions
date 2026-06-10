class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixPdt=[]
        suffixPdt=[0]*len(nums)
        ans=[]

        prefixPdt.append(1)
        pdt=1
        for i in range(len(nums)-1):
            prefixPdt.append(pdt*nums[i])
            pdt*=nums[i]

        pdt=1
        for i in range(len(nums)-1,-1,-1):
            suffixPdt[i]=pdt
            pdt*=nums[i]

        for i in range(len(nums)):
            ans.append(prefixPdt[i]*suffixPdt[i])

        return ans
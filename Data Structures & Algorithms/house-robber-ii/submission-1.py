class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1,nums2=nums[1:],nums[:len(nums)-1]
        if len(nums)==1:
            return nums[0]
        
        def robbing(nums):
            rob1,rob2=0,0
            for n in nums:
                temp=max(n+rob1,rob2)
                rob1=rob2
                rob2=temp

            return rob2

        return max(robbing(nums1),robbing(nums2))

        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        ans=nums[0]

        while low<=high:
            mid=(low+high)//2

            # check if array is sorted
            if nums[low]<=nums[high]:
                ans=min(ans,nums[low])

            # if nums[mid]<=nums[low]:
            #     ans=min(ans,nums[mid])

            if nums[mid]<=nums[high]: #nums[mid] is in the right part, search the left part
                ans=min(ans,nums[mid]) # sometimes nums[mid] might be the min no.
                high=mid-1

            else: # nums[mid] is in the left part=> search the right part
                ans=min(ans,nums[mid])
                low=mid+1

        return ans
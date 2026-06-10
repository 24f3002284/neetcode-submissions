class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high=0,len(nums)-1
        mid=low+(high-low)//2
        res=float('inf')

        while low<=high:
            mid=low+(high-low)//2

            if nums[low]<=nums[high]:
                res=min(res,nums[low])
                return res
            if nums[low]<=nums[mid]: #left part is sorted=> check the right part
                res=min(nums[low],res)
                low=mid+1
            else:
                res=min(res,nums[mid])
                high=mid-1

        return res
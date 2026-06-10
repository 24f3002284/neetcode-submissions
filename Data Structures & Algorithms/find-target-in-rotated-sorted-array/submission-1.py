class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1

        # while low<=high:
        #     mid=(low+high)//2

        #     # if nums[low]<=nums[high]: # already sorted
        #     #     if nums[mid]==target:
        #     #         return mid
        #     #     elif nums[mid]>target:
        #     #         high=mid-1
        #     #     else:
        #     #         low=mid+1

        #     # else:
        #         # nums[mid] is in the left sorted half => check iftarget is in the left sorted half. if present, do bin search on left half, else check right half

        #     if nums[mid]>=nums[low]: # nums[mid] is in the left sorted half
        #         # if target<=nums[mid] and nums[low]<=target:
        #         if target>=nums[low]:
        #             high=mid
        #         else:
        #             low=mid+1

        #     else: # search the left half
        #         # if target>=nums[mid] and target<=nums[high]:
        #         if target>=nums[high]:
        #             high=mid
        #         else:
        #             low=mid+1

        # return -1

        # # low,high=0,len(nums)-1
        # # while low<=high:
        # #     mid=(low+high)//2

        # #     if nums[mid]==target:
        # #         return mid

        # #     if nums[mid]>target:

        # #         high=mid-1

        # #     else:
        # #         low=mid+1

        # # return -1

        while low<=high: # = is imp for singleton arrays
            mid=(low+high)//2

            if nums[mid]==target:
                return mid

            # one of the halves will be sorted.
            # case 1: left half is sorted
            if nums[low]<=nums[mid]:
                if target>nums[mid]:
                    low=mid+1
                elif target<nums[low]:
                    low=mid+1
                else:
                    high=mid-1

            else: # right part is sorted
                if target<nums[mid] or target>nums[high]:
                    high=mid-1
                else:
                    low=mid+1

        return -1

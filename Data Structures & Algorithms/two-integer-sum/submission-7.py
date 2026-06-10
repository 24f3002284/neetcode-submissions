class Solution:
    def twoSum(self, nums: List[int], target: int):
        prevMap=collections.defaultdict(list)

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]

            prevMap[n]=i # storing indices of each number in nums

        # return [-1,-1]
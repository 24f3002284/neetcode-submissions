class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(n) TC AND SC
        hashSet=set()
        for n in nums:
            hashSet.add(n)

        l=len(nums)
        for n in range(l+1):
            if n not in hashSet:
                return n

        # return hashSet.pop()
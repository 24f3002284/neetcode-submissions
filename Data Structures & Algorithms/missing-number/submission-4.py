class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashSet=set()
        for n in nums:
            hashSet.add(n)

        for i in range(len(nums)+1):
            if i not in hashSet:
                return i
        return len(nums)+1
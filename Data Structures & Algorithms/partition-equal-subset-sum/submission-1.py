class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        target=sum(nums)//2
        
        sums=set()
        sums.add(0)

        for n in nums:
            for s in list(sums):
                sums.add(n+s)

            if target in sums:
                return True

        return False
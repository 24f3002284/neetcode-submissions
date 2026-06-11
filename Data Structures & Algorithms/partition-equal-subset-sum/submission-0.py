class Solution:
    def canPartition(self, nums: List[int]) -> bool:      
        if sum(nums)%2==1:
            return False

        target=sum(nums)//2        
        sums=set()
        sums.add(0) #imp!! zero can always be a sum 

        for n in nums:

            for s in list(sums):
                sums.add(s+n)

            if target in sums:
                return True

        return False

    


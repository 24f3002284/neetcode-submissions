class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        ans=0

        while low<=high:
            mid=(low+high)//2 # rate at which koko eats the banana
            timeTaken=0
            for p in piles:
                if p%mid==0:
                    timeTaken+=int(p/mid)
                else:
                    timeTaken+=int(p/mid)+1

            if timeTaken>h:
                low=mid+1

            else:
                ans=mid
                high=mid-1

        return ans

            
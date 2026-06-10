class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles) # low is not min(piles)
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

        # low,high=0,len(piles)-1
        # ans=0
        # piles.sort()

        # while low<=high:
        #     mid=(low+high)//2

        #     timeTaken=0
        #     for n in piles:
        #         if n%piles[mid]==0:
        #             timeTaken+=int(n/piles[mid])
        #         else:
        #             timeTaken+=int(n/piles[mid])+1

        #     if timeTaken>h:
        #         low=mid+1
        #     else:
        #         ans=piles[mid]
        #         high=mid-1

        # return ans

            

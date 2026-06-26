class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*n
        prices[src]=0#cost to reach first node=src, we r already there

        for i in range(k+1): #k stops-allowed => run BF(Bellman Ford algo. (k+1) times)
            tmpPrices=prices.copy()
            for s,d,p in flights:#during each iteration of the BF algo, loop through all edges
                if prices[s]==float('inf'):#s cant be reached, the cost to reach any city from s will remain infinity, if we go through this path
                    continue
                elif prices[s]+p<tmpPrices[d]:
                    tmpPrices[d]=prices[s]+p #tot price to reach s+price to reach d from s

            prices=tmpPrices
        
        return prices[dst] if prices[dst]!=float('inf') else -1

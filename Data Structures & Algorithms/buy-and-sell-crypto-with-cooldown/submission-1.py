class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp={}

        def maximumProfit(day,canBuy):
            if (day,canBuy) in dp:
                return dp[(day,canBuy)]
            if day>=n:
                return 0

            if canBuy==True:# 2 cases are possible=> either buy or cooldown
                buy=maximumProfit(day+1,not canBuy)-prices[day] #can't buy after we bought a
                cooldown=maximumProfit(day+1,canBuy)
                # return max(buy,cooldown)
                dp[(day,canBuy)]=max(cooldown,buy)

            else:
                sell=maximumProfit(day+2,not canBuy)+prices[day] #can buy only after 1 cooldown day=>day+2. 
                cooldown=maximumProfit(day+1,canBuy) #cannot buy on day+1 since it is cooldown
                # return max(sell,cooldown)
                dp[(day,canBuy)]=max(sell,cooldown)

            return dp[(day,canBuy)]
            
        return maximumProfit(0,True)
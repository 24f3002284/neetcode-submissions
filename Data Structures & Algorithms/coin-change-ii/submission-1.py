class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp={}

        def dfs(idx,amt):
            if amt==0:
                return 1
            if idx==0 or amt<0:
                return 0
            
            if (idx,amt) in dp:
                return dp[(idx,amt)]

            dp[(idx,amt)]=(dfs(idx-1,amt)+dfs(idx,amt-coins[idx-1]))
            return dp[(idx,amt)]

        return dfs(n,amount)
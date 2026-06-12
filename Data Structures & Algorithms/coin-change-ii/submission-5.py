class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)

        # def dfs():
        dp=[[0]*(n+1) for i in range(amount+1)]

        for j in range(n):
            dp[amount][j]=1

        for i in range(amount-1,-1,-1):
            for j in range(n-1,-1,-1):
                use_coin=0
                if i+coins[j]<=amount:
                    use_coin=dp[i+coins[j]][j]
                skip_coin=dp[i][j+1]
                dp[i][j]=use_coin+skip_coin

        return dp[0][0]

        # return dfs(n-1,amount)
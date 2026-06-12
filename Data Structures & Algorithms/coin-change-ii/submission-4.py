class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case: tot == amount → 1 (for any idx)
        for idx in range(n + 1):
            dp[idx][amount] = 1

        # Fill in reverse order of recursion
        for idx in range(n - 1, -1, -1):
            for tot in range(amount - 1, -1, -1):
                use_coin = dp[idx][tot + coins[idx]] if tot + coins[idx] <= amount else 0
                skip_coin = dp[idx + 1][tot]
                dp[idx][tot] = use_coin + skip_coin

        return dp[0][0]
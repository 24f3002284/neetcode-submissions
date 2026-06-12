class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        n=len(coins)

        def dfs(idx,tot):
            if (idx,tot) in dp:
                return dp[(idx,tot)]

            if tot==amount:
                return 1
            if idx==n or tot>amount:
                return 0

            dp[(idx,tot)]=dfs(idx,tot+coins[idx])+dfs(idx+1,tot)
            return dp[(idx,tot)]

        return dfs(0,0)
import sys
sys.setrecursionlimit(100000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        directions=[[0,1],[0,-1],[-1,0],[1,0]]
        dp=[[-1]*cols for _ in range(rows)]

        def dfs(row,col):
            if dp[row][col]!=-1:
                return

            dp[row][col]=1 #imp!! mark the current cell as visited before exploring  its neighbors.
            for dx,dy in directions:
                r,c=row+dx,col+dy

                if r not in range(rows) or c not in range(cols) or matrix[r][c]<=matrix[row][col]:
                    continue
                
                if dp[r][c]!=-1:
                    dp[row][col]=max(dp[row][col],1+dp[r][c])
                else:
                    dfs(r,c)
                    dp[row][col]=max(dp[row][col],1+dp[r][c])

            dp[row][col]=max(1,dp[row][col])

        for r in range(rows):
            for c in range(cols):
                dfs(r,c)

        ans=0
        for r in range(rows):
            for c in range(cols):
                ans=max(ans,dp[r][c])

        return ans
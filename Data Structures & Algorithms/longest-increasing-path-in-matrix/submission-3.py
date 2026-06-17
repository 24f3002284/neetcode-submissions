import sys
sys.setrecursionlimit(100000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        dp = {}  # (row, col) -> longest path length

        def dfs(row, col):
            if (row, col) in dp:
                return dp[(row, col)]

            dp[(row, col)] = 1  # at minimum, path length is 1 (just itself)

            for dx, dy in directions:
                r, c = row + dx, col + dy

                if r not in range(rows) or c not in range(cols) or matrix[r][c] <= matrix[row][col]:
                    continue

                dp[(row, col)] = max(dp[(row, col)], 1 + dfs(r, c))

            return dp[(row, col)]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)

        return max(dp.values())
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        visited=set()
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            visited.add((r,c))
            area=1

            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1 and (row,col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))
                        area+=1

            return area     

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and (row,col) not in visited:
                    ans=max(ans,bfs(row,col))

        return ans
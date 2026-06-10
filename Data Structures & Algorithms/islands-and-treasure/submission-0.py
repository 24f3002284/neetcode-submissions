class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def addCell(row,col):
            if row not in range(rows) or col not in range(cols) or grid[row][col]==-1 or (row,col) in visited:
                return

            q.append((row,col))
            visited.add((row,col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist

                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r,c-1)
                addCell(r-1,c)
            dist+=1  


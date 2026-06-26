class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))

        level=1
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dirs:
                    newR,newC=r+dr,c+dc

                    if newR not in range(rows) or newC not in range(cols) or grid[newR][newC]==-1 or grid[newR][newC]==0:
                        continue

                    if grid[newR][newC]>level:
                        grid[newR][newC]=level
                        q.append((newR,newC)) #DG!! IMP!

            level+=1

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands=0
        rows,cols=len(grid),len(grid[0])
        visited=set()

        def bfs(row,col):
            q=collections.deque()
            
            # row,col=r,c
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            q.append((row,col))
            # visited.add((row,col))

            while q:
                row,col=q.popleft() # replace with .pop() for dfs

                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]=="1":
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    bfs(r,c)

        return islands
    
            

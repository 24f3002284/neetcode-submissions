class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        visited=set()
        rows,cols=len(grid),len(grid[0])
        # directions=[[0,1],[1,0],[0,-1],[-1,0]]

        def makeRotten(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]==0 or (r,c) in visited: # can'ttraverse through it
                return

            q.append((r,c))
            visited.add((r,c))
            grid[r][c]=2 #imp!! mark it as rotten, only then can we return -1
            return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    q.append((row,col)) # adding rotten fruits into q
                    visited.add((row,col)) #adding rotten fruits into visited

        time=-1 # imp!! not time=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                
                makeRotten(r+1,c)
                makeRotten(r,c+1)
                makeRotten(r-1,c)
                makeRotten(r,c-1)
            time+=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1

        return max(time,0) # imp!! bcz if a grid is empty, return 0(time taken) and not -1

                


        
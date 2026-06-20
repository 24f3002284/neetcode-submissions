class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # adjL
        visited=set()
        n=len(grid)

        minHeap=[[grid[0][0],0,0]] # max val upuntill now,row,col
        visited=set()
        visited.add((0,0))
        
        while minHeap:
            time,r,c=heapq.heappop(minHeap)
            if r==n-1 and c==n-1:
                return time

            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            
            for dr,dc in directions:
                neiR,neiC=r+dr,c+dc

                if neiR not in range(n) or neiC not in range(n) or (neiR,neiC) in visited:
                    continue

                heapq.heappush(minHeap,[max(time,grid[r+dr][c+dc]),r+dr,c+dc])
                visited.add((r+dr,c+dc))


            
                    
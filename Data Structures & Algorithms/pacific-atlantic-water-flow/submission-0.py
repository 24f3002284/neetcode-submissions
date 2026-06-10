class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,atl=set(),set()
        # qPac,qAtl=deque(),deque()
        rows,cols=len(heights),len(heights[0])
        visPac,visAtl=set(),set()

        def dfs(r,c,visited,prevHgt):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c]<prevHgt:
                return

            # q.append((r,c))
            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for col in range(cols):
            # qPac.append((0,col))
            # qAtl.append((rows-1,col))
            dfs(0,col,visPac,heights[0][col])
            dfs(rows-1,col,visAtl,heights[rows-1][col])

        for row in range(rows):
            # qPac.append((row,0))
            # qAtl.append((row,cols-1))
            dfs(row,0,visPac,heights[row][0])
            dfs(row,cols-1,visAtl,heights[row][cols-1])

        ans=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visPac and (r,c) in visAtl:
                    ans.append([r,c])

        return ans

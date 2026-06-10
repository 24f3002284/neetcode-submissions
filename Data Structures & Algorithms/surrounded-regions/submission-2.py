class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #core idea=>mark border Os and Os connecting border Os using '#'. change all Os(which didnot get converted to #) to X. finally change all # to O. 
        
        q=deque()
        rows,cols=len(board),len(board[0])
        visited=set()

        def bfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c]!="O":
                return

            visited.add((r,c))
            board[r][c]='#'
            q.append((r,c)) #add it to q so that its neighbors get explored

        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c]=="O":
                    q.append((r,c)) # initialising q with border Os
                    board[r][c]="#"

        while q:
            # for i in range(len(q)):
            r,c=q.popleft()

            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c-1)
            bfs(r,c+1)
            

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='#':
                    board[i][j]='O'

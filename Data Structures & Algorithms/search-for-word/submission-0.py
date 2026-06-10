class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visited=set()

        def backtracking(r,c,idx):
            if idx==len(word):
                return True

            if r not in range(rows) or c not in range(cols) or (r,c) in visited or word[idx]!=board[r][c]:
                return False

            visited.add((r,c))

            found=(backtracking(r+1,c,idx+1) or 
                    backtracking(r,c+1,idx+1) or
                    backtracking(r-1,c,idx+1) or
                    backtracking(r,c-1,idx+1))

            visited.remove((r,c))# backtracking
            
            return found

        for r in range(rows):
            for c in range(cols):
                if backtracking(r,c,0):
                    return True

        return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        blocks=collections.defaultdict(set) # keys=(row//3,col//3)
        
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    continue

                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in blocks[(i//3,j//3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                blocks[(i//3,j//3)].add(board[i][j])

        return True
                
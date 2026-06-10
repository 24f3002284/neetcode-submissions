class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        colSet=set()
        negDiagSet=set()
        posDiagSet=set()

        def backtracking(row,board):
            if row==n:
                copy=["".join(row) for row in board]
                ans.append(copy.copy())
                return

            for col in range(n):
                if col in colSet or row+col in negDiagSet or row-col in posDiagSet:
                    continue

                colSet.add(col)
                negDiagSet.add(row+col)
                posDiagSet.add(row-col)
                board[row][col]="Q"
                backtracking(row+1,board) #DF!

                # backtracking
                colSet.remove(col)
                negDiagSet.remove(row+col)
                posDiagSet.remove(row-col)
                board[row][col]="."

        # for row in range(n):
        #     backtracking(row,board) noneed of for loop
        backtracking(0,board)

        return ans
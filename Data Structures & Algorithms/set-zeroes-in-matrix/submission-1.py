class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: #O(M+N)=TC
        rows=[1 for i in range(len(matrix))]
        cols=[1 for i in range(len(matrix[0]))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    rows[r]=0
                    cols[c]=0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if rows[r]==0 or cols[c]==0:
                    matrix[r][c]=0

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # O(log(m*n)) =>use bin search for the overall matrix
        # numbers=[]

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         numbers.append(matrix[i][j])

        # low,high=0,len(matrix)*len(matrix[0])-1 #imp note the -1

        # while low<=high:
        #     mid=(low+high)//2

        #     if(numbers[mid]==target):
        #         return True
        #     if(numbers[mid]<target):
        #         low=mid+1
        #     else:
        #         high=mid-1

        # return False       
        
        # O(log m)+O(log n)
        reqdRow=0

        lowRow,highRow=0,len(matrix)-1
        lastCol,firstCol=len(matrix[0])-1,0

        while lowRow<=highRow:
            midRow=(lowRow+highRow)//2

            if target<=matrix[midRow][lastCol] and matrix[midRow][firstCol]<=target:
                reqdRow=midRow
                break

            elif target>matrix[midRow][firstCol]:
                lowRow=midRow+1
            else:
                highRow=midRow-1

        while firstCol<=lastCol:
            midCol=(firstCol+lastCol)//2

            if matrix[reqdRow][midCol]==target:
                return True

            elif matrix[reqdRow][midCol]>target:
                lastCol=midCol-1

            else:
                firstCol=midCol+1

        return False
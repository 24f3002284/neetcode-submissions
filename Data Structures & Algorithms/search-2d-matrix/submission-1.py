class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n)) =>use bin search for the overall matrix
        numbers=[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                numbers.append(matrix[i][j])

        low,high=0,len(matrix)*len(matrix[0])-1

        while low<=high:
            mid=(low+high)//2

            if(numbers[mid]==target):
                return True
            if(numbers[mid]<target):
                low=mid+1
            else:
                high=mid-1

        return False        
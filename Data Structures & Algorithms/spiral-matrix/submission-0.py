class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom=0,len(matrix) # the last indices, right and bottom shd be 1 more than the last idx
        left,right=0,len(matrix[0]) 
        ans=[]

        while left<right and top<bottom:
            # add no.s in the top row
            for i in range(left,right):
                ans.append(matrix[top][i])
            top+=1

            # add no.s in the right col
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right-=1

            if left>=right or top>=bottom:
                break
                
            #add no.s of the bottom row
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom-=1

            # no.s of the left col
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
            left+=1

        return ans
            

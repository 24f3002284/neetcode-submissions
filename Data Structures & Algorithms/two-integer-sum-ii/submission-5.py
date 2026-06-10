class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1

        for i,n in enumerate(numbers):
            tar=target-n

            while j>i:
                if(numbers[j]==tar):
                    return [i+1,j+1]
                elif(numbers[j]>tar):
                    j-=1
                else:
                    break
                
        return [-1,-1]
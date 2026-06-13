class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()

        while n not in visited:
            sum=0
            visited.add(n)
            while(n>0):
                sum+=(n%10)**2
                n//=10
            
            if sum==1:
                return True

            n=sum
            
            
        return False
        
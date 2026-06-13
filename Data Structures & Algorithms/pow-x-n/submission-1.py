class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def recFn(x,n):
            if n<0:
                return 1/recFn(x,-n)

            if n==0:
                return 1
            if n%3==0:
                return recFn(x*x*x,n//3)
            elif n%3==1:
                return x*recFn(x*x*x,n//3)
            else:
                return x*x*recFn(x*x*x,n//3)

        return recFn(x,n)

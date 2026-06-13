class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def recFn(x,n):
            if n<0:
                return 1/recFn(x,-n)

            if n==0:
                return 1
            if n%2==0:
                return recFn(x*x,n//2)
            else:
                return x*recFn(x*x,n//2)

        return recFn(x,n)

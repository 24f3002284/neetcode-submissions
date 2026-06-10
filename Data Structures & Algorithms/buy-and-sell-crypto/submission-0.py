class Solution:
    def maxProfit(self, prices: List[int]) -> int:     
        # leftMin=[0]
        # rightMax=[0]*(len(prices))
        # n=len(prices)

        # for i in range(1,n):
        #     leftMin.append(min(leftMin[i-1],prices[i-1]))

        # for i in range(n-2,-1,-1):
        #     rightMax[i]=max(rightMax[i+1],prices[i+1])

        # best=0
        # for i in range(n):
        #     if leftMin[i]<rightMax[i]:
        #         best=max(best,rightMax[i]-leftMin[i])
        
        # return best

        stack=[]
        minimum=1e8
        best=0

        for n in prices:
            if n<minimum:
                minimum=n
                
            else:
                best=max(best,n-minimum)

        return best

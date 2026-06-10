class Solution:
    def trap(self, height: List[int]) -> int:
        # n=len(height)
        # maxLeft=[0]*n
        # maxRight=[0]*n

        # for i in range(1,n):
        #     maxLeft[i]=max(maxLeft[i-1],height[i-1])

        # for i in range(n-2,-1,-1):
        #     maxRight[i]=max(maxRight[i+1],height[i+1])

        # # we find the minimum of the leftMax and rightMax till the current index and subtract current height from it. thip is the amount(height) of water that can be stored in the current index.
        # # summation of all such heights give the total amount of water that can be trapped.

        # trapped=0
        # for i in range(n):
        #     if(min(maxLeft[i],maxRight[i])>height[i]):
        #         trapped+=min(maxLeft[i],maxRight[i])-height[i]

        # return trapped

        l,r=0,len(height)-1
        leftMax,rightMax=height[l],height[r]
        trapped=0

        while(l<r):
            if(leftMax<rightMax):
                l+=1
                leftMax=max(leftMax,height[l])
                trapped+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                trapped+=rightMax-height[r]

        return trapped

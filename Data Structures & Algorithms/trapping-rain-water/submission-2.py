class Solution:
    def trap(self, height: List[int]) -> int:
        trapped=0

        l,r=0,0
        leftMax=[0]*len(height)
        rightMax=[0]*len(height)

        for i in range(1,len(height)):
            leftMax[i]=max(leftMax[i-1],height[i-1])

        for i in range(len(height)-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i+1])

        for i in range(len(height)):
            if(min(rightMax[i],leftMax[i])>height[i]):
                trapped+=min(rightMax[i],leftMax[i])-height[i]

        return trapped
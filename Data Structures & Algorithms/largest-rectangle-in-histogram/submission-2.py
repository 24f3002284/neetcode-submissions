class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxArea=0

        for i in range(len(heights)):
            # cnt=0
            start=i
            while st and st[-1][1]>heights[i]:
                maxArea=max(maxArea,(i-st[-1][0])*st[-1][1])
                start=st[-1][0]
                st.pop()
                # cnt+=1
                

            # st.append((i-cnt,heights[i]))
            st.append((start,heights[i]))

        # now st contains all those hgts which can be extended

        while st:
            # (pos,hgt)=st[-1]

            maxArea=max(maxArea,(len(heights)-st[-1][0])*st[-1][1])
            st.pop()

        return maxArea
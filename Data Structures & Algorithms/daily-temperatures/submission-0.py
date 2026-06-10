class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i]>st[-1][0]:
                ans[st[-1][1]]=i-st[-1][1]
                st.pop()

            st.append((temperatures[i],i))

        return ans
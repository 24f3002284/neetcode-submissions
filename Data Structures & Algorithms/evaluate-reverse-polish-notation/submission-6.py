class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations=['+','-','*','/']
        st=[]

        for ch in tokens:
            if(ch not in operations):
                st.append(int(ch))

            else:
                b=st[-1]
                st.pop()
                a=st[-1]
                st.pop()

                if(ch=='+'):
                    st.append(a+b)
                elif(ch=='-'):
                    st.append(a-b)
                elif ch=='*':
                    st.append(a*b)
                else:
                    st.append(int(a/b))

        return st[0]

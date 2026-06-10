class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        for ch in s:
            if ch in ['{','(','[']:
                st.append(ch)

            elif len(st)==0:
                return False

            else:
                if ch==')' and st[-1]=='(':
                    st.pop()
                elif ch==']' and st[-1]=='[':
                    st.pop()
                elif ch=='}' and st[-1]=='{':
                    st.pop()
                else:
                    return False

        if len(st)!=0:
            return False

        return True              
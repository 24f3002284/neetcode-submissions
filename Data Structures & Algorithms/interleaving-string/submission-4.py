class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo={}

        def interl(i1,i2):
            if (i1,i2) in memo:
                return memo[(i1,i2)]
            if i1+i2==len(s3):
                return i1==len(s1) and i2==len(s2)

            i3=i1+i2
            result=False
            if i1<len(s1) and s1[i1]==s3[i3]:
                result=interl(i1+1,i2)                

            if not result and i2<len(s2) and s2[i2]==s3[i1+i2]:
                result=interl(i1,i2+1)

            memo[(i1,i2)]=result
            return result

            # if (i1+i2)>len(s3):
            #     return True
            # if i1>=len(s1):
            #     return s2[i2:]==s3[(i1+i2):]
            # elif i2>=len(s2):
            #     return s1[i1:]==s3[(i1+i2):]
            # else:
            #     if s1[i1]==s3[(i1+i2)]:
            #         return interl(i1+1,i2)
            #     elif s2[i2]==s3[i1+i2]:
            #         return interl(i1,i2+1)
            #     else:
            #         return False

        return interl(0,0)
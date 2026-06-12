class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
                return False

        dp={}
        def dfs(i1,i2):
            if (i1,i2) in dp:
                return dp[(i1,i2)]
            
            if i1==len(s1):
                return s2[i2:]==s3[i1+i2:]
            elif i2==len(s2):
                return s1[i1:]==s3[i1+i2:]

            if s1[i1]!=s3[(i1+i2)] and s2[i2]!=s3[(i1+i2)]:
                return False
            if s1[i1]==s3[(i1+i2)] and s2[i2]!=s3[(i1+i2)]:
                dp[(i1,i2)]= dfs(i1+1,i2)
            elif s2[i2]==s3[(i1+i2)] and s1[i1]!=s3[(i1+i2)]:
                dp[(i1,i2)]= dfs(i1,i2+1)
            else:
                dp[(i1,i2)]=dfs(i1,i2+1) or dfs(i1+1,i2)

            return dp[(i1,i2)]

        return dfs(0,0)
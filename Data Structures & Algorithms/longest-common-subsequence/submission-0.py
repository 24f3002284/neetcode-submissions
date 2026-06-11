class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2=len(text1),len(text2)
        dp=[[0]*(l1+1) for i in range(l2+1)]

        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[j][i]=1+dp[j+1][i+1]
                else:
                    dp[j][i]=max(dp[j][i+1],dp[j+1][i])

        return dp[0][0]
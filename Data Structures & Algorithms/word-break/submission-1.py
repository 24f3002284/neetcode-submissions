class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False for i in range(n+1)] # indices of dp can be from 0,1,2,3..n-1,n

        dp[n]=True # if we reach the end of s, the idx after n-1, => successful=>T
        for i in range(n-1,-1,-1):
            for w in wordDict:
                if i+len(w)-1<n and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]==True:
                    break

        return dp[0]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        minLength=float('inf')
        ans=""

        countT={}
        curWindow={}
        for ch in t:
            countT[ch]=countT.get(ch,0)+1

        l=0

        have,need=0,len(countT) # need= no. of distinct chrctrs in freqT

        for r in range(len(s)):
            curWindow[s[r]]=curWindow.get(s[r],0)+1

            if s[r] in countT and curWindow[s[r]]==countT[s[r]]:
                have+=1

            while have==need:
                if (r-l+1)<minLength:
                    ans=s[l:r+1]
                    minLength=r-l+1 # imp! update minLength
                    
                curWindow[s[l]]-=1

                if s[l] in countT and countT[s[l]]>curWindow[s[l]]:
                    have-=1
                l+=1

        return ans

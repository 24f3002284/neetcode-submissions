class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        freqMap={}
        length=0

        while(r<len(s)):
            while s[r] in freqMap and freqMap[s[r]]>=l:
                freqMap[s[l]]=-1
                l+=1

            freqMap[s[r]]=r
            length=max(length,r-l+1)
            r+=1

        return length

        
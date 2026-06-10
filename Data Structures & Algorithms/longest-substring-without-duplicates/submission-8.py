class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window of variable size=> add, shrink, record 
        l,r=0,0
        curWind=set()
        maxLeng=0

        while r<len(s):
            while s[r] in curWind:
                curWind.remove(s[l])
                l+=1

            curWind.add(s[r])
            maxLeng=max(maxLeng,r-l+1)
            
            r+=1

        return maxLeng
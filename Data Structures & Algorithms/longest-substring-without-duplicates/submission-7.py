class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet=set()
        l,r=0,0
        ans=0

        while r<len(s):
            while s[r] in sSet:
                sSet.remove(s[l])
                l+=1

            sSet.add(s[r])
            ans=max(ans,r-l+1)
            r+=1

        return ans
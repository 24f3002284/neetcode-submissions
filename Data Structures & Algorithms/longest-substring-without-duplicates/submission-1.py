class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        n=len(s)

        seen={}

        longest=0

        for r,ch in enumerate(s):
            if ch in seen and seen[ch]>=l:
                l=seen[ch]+1

            seen[ch]=r
            longest=max(longest,r-l+1)

        return longest
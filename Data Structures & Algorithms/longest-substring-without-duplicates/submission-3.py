class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l,r=0,0
        # n=len(s)

        # seen={}

        # longest=0

        # for r,ch in enumerate(s): 
        #     if ch in seen and seen[ch]>=l:
        #         l=seen[ch]+1

        #     seen[ch]=r
        #     longest=max(longest,r-l+1)

        # return longest

        l=0
        r=0
        n=len(s)

        longest=0
        dict={}

        while r<n:
            if(s[r] in dict and dict[s[r]]>=l):
                l=dict[s[r]]+1
            dict[s[r]]=r

            longest =max(longest,r-l+1)
            r+=1

        return longest
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        freq={}
        maxLeng=0
        ans=""

        while r<len(s):
            freq[s[r]]=freq.get(s[r],0)+1

            if r-l+1-max(freq.values())>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1

            if r-l+1>maxLeng:
                maxLeng=r-l+1
                ans=s[l:r+1]

            r+=1

        return maxLeng
                
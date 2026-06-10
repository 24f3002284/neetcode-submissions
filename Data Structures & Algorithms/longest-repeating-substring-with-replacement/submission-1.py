class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        l,r=0,0

        mp=collections.defaultdict(int)
        curWindLen=0

        while(r<len(s)):
            mp[s[r]]=mp.get(s[r],0)+1
            curWindLen+=1

            maxFreq=0
            for ch in mp:
                if mp[ch]>maxFreq:
                    maxFreq=mp[ch]
                
            if(curWindLen-maxFreq<=k):
                ans=max(ans,curWindLen)

            else:
                
                mp[s[l]]-=1
                l+=1 # increment this only after updating line no. 23 (the map)
                curWindLen-=1

            r+=1

        return ans  


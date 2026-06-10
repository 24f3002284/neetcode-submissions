class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        freqs=collections.defaultdict(set)
        freqt=collections.defaultdict(set)

        # freqt={}
        # freqs={}

        for ch in s:
            if ch in freqs:
                freqs[ch]+=1
            else:
                freqs[ch]=1

        for ch in t:
            if ch in freqt:
                freqt[ch]+=1
            else:
                freqt[ch]=1

        return freqs==freqt
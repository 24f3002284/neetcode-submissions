class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}

        for ch in s:
            freqs[ch]=freqs.get(ch,0)+1
        
        for ch in t:
            freqt[ch]=freqt.get(ch,0)+1

        return freqs==freqt
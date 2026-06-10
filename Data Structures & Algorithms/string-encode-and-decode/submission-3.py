class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            length=len(s)
            res+=str(length)+'#'+s #not res=str(length)+'#'+s

        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        
        while(i<len(s)):
            j=i+1

            while(s[j]!='#'):
                j+=1

            length=int(s[i:j])

            res.append(s[j+1:j+1+length])
            i=j+1+length

        return res #dont forget intendation
            
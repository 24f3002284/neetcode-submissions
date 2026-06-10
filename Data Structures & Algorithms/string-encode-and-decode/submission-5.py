class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        
        for s in strs:
            length=len(s)

            ans+=str(length)+'#'+s

        return ans

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0

        while(i<len(s)):
            j=i+1 # finding hash

            while s[j]!='#':
                j+=1

            # now j points to # and i points to the beginning of the length of the word
            length=int(s[i:j])

            ans.append(s[j+1:j+1+length])
            i=(j+1+length)

        return ans

            
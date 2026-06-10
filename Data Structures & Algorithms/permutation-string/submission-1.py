class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1=[0]*26
        dict2=[0]*26

        for ch in s1:
            dict1[ord(ch)-ord('a')]+=1

        l,r=0,len(s1)-1
        for k in range(l,r):
            dict2[ord(s2[k])-ord('a')]+=1

        while r<len(s2):
            dict2[ord(s2[r])-ord('a')]+=1          

            flag=True

            for i in range(26):
                if(dict1[i]!=dict2[i]):
                    flag=False
                    break

            if(flag==True):
                return True

            dict2[ord(s2[l])-ord('a')]-=1           
            
            r+=1
            l+=1

        return False

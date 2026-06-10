class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]

        def backtracking(idx,cur:list):
            if idx==len(s): #starting idx=idx
                ans.append(cur.copy())
                return

            if idx>len(s):
                return

            for j in range(idx+1,len(s)+1): # ending idx=j
                if isPali(s,idx,j-1):
                    cur.append(s[idx:j])
                    backtracking(j,cur)
                    cur.pop()

        def isPali(s,i,j):
            # l,r=i,j+
            # while l>=i and r<j:
            #     if s[l]!=s[r]:
            #         return False
            #     l-=1
            #     r+=1
            l,r=i,j
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1

            return True

        backtracking(0,[])
        return ans            
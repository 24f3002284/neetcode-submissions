class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        closed,open=0,0
        ans=[]

        def backtracking(closed,open,cur:list):
            if closed>open:
                return

            if len(cur)==2*n:
                ans.append("".join(cur))
                return

            if open<n:
                cur.append("(")
                backtracking(closed,open+1,cur)
                cur.pop() #dont miss out
                
            if closed<open:
                cur.append(")")
                backtracking(closed+1,open,cur)
                cur.pop() #dont miss out on this

        backtracking(0,0,[])
        return ans
            


            


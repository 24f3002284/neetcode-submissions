class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        ans=[]
        if not digits:
            return ans

        digToChar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(curStr,idx):
            if idx==len(digits): # or len(curStr)==len(digits)
                ans.append(curStr)
                return

            for ch in digToChar[digits[idx]]:
                backtrack(curStr+ch,idx+1)

        backtrack("",0)
        return ans
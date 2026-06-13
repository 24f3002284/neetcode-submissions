class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        i=n-1
        carry=1
        ans=[]

        while i>=0 or carry>0:
            sum=0
            sum+=digits[i] if i>=0 else 0
            sum+=carry
            ans.append(sum%10)
            carry=sum//10
            
            i-=1

        ans.reverse()
        return ans

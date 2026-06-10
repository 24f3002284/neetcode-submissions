class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for ch in s:
            if ch.isalnum():
                new_s+=ch

        new_s=new_s.lower()
        return new_s[::]==new_s[::-1]
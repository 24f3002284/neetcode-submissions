class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        
        for n in nums:
            
            if (n-1) not in numSet:
                # begining of a sequence
                #check if n+1 is present in numSet. if present, increase curLength
                curLength=1

                while(n+1 in numSet):
                    curLength+=1
                    n+=1

                longest=max(longest,curLength)

        return longest

            

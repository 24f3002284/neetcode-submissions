class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we have to 1st check if the current number is at the beg of any sequence, only then will we able to create the longest consec. seq. using it
        # to prevent O(n2), use set

        longest=0
        
        numSet=set(nums)
        for n in numSet: # so that we donot have to repeat for each duplicate
            if (n-1) not in numSet: # new seq begins
                cur=1 # current length=1(the current element)
                while (n+1) in numSet:
                    cur+=1
                    n+=1
                longest=max(longest,cur)
        
        return longest
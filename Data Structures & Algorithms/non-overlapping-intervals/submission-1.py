class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # prevEnd=intervals[0][1] write after we sort intervals!!
        ans=0
        intervals.sort()
        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if start<prevEnd:#one of them has to be deleted.
                ans+=1
                prevEnd=min(prevEnd,end)#better delete the one that ends first, so that it allows less no. of intervals to be deleted                ans+=1

            else:
                prevEnd=end

        return ans
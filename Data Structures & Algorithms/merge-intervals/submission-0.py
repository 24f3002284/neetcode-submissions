class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]

        prevEnd=intervals[0][1]
        start=intervals[0][0]
        
        for s,e in intervals[1:]:
            if s<=prevEnd:
                prevEnd=max(prevEnd,e)

            else:
                ans.append([start,prevEnd])
                start=s
                prevEnd=e

        ans.append([start,prevEnd])
        return ans
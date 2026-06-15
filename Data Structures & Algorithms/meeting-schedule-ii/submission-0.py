"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])
        
        sp,ep=0,0
        cnt,ans=0,0

        while sp<len(intervals):
            if start[sp]<end[ep]:
                sp+=1
                cnt+=1
            else:
                ep+=1
                cnt-=1

            ans=max(ans,cnt)

        return ans
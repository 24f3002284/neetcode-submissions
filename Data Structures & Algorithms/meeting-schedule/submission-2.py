"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda p:p.start)

        prevEnd=intervals[0].end#before this, check if there exists an interval in intervals

        for inter in intervals[1:]:
            if inter.start<prevEnd:
                return False
            else:
                prevEnd=inter.end

        return True
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        res = 0
        count = 0
        s_ptr, e_ptr = 0, 0
        while s_ptr < len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                count += 1
                s_ptr += 1
            else:
                count -= 1
                e_ptr += 1
            res = max(count, res)
        return res
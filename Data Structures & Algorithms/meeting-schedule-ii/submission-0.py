"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap =[]
        for i in intervals:
            #store the smallest end time
            if heap and i.end < heap[0]:
                heapq.heappush(heap, i.end)
            elif heap and i.start>=heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,i.end)
            else:
                heapq.heappush(heap,i.end)
        return len(heap)

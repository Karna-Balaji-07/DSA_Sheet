# Divide Intervals into Minimum Number of Groups
import heapq
def solution(intervals):
    intervals.sorT(key=lambda x : x[0])
    heap = []
    for interval in intervals:
        if heap and heap[0] < interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,interval[1])
    return len(heap)
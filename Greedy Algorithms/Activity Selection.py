# Activity selection

def solution(start, end):
    arr = list(zip(start,end))
    arr.sort(key=lambda x : x[1])
    count = 1
    j = 0
    for i in range(1, len(arr)):
        if arr[i][0] > arr[j][1]:
            count += 1
            j += 1
    return count

import heapq as heap
def solution(start, end):
    result = 0
    arr = []
    for i in range(len(start)):
        heap.heappush(arr, (end[i],start[i]))
        
    finish = -1
    while arr:
        activity = heap.heappop(arr)
        if activity[1] > finish:
            result += 1
            finish = activity[0]
        
    return result
        
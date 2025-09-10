# task scheduler


import heapq as heap
from collections import Counter, deque
def solution(arr,n):
    freq = Counter(arr)
    maxheap = [-x for x in freq.values()]
    heap.heapify(maxheap)
    time = 0
    cooldown = deque()
    while maxheap or cooldown:
        time += 1
        if maxheap:
            count = heap.heappop(maxheap)+1
            if count != 0:
                cooldown.append((time+n,count))
        if cooldown and cooldown[0][0] == time:
            _, ready = cooldown.popleft()
            heap.heappush(maxheap, ready)
        
    return time

tasks = ["A","A","A", "B","B","B"]
n = 3
print(solution(tasks,n))
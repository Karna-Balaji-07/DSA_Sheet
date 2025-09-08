# Job sequencing

import heapq as heap
def solution(deadline, profit):
    n = len(deadline)
    ans = [0,0]
    jobs = [(deadline[i], profit[i]) for i in range(n)]
    jobs.sort()
    arr = []
    for job in jobs:
        if job[0] > len(arr):
            heap.heappush(arr, job[1])
        elif arr and arr[0] < job[1]:
            heap.heappop(arr)
            heap.heappush(arr, job[1])
        
    while arr:
        ans[1] += heap.heappop(arr)
        ans[0] += 1
    return ans

deadline = [3, 1, 2, 2]; profit = [50, 10, 20, 3]
print(solution(deadline, profit))
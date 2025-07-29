# 436. Find Right Interval

def solution(arr):
    starts = [(arrs[0],i) for i,arrs in enumerate(arr)]
    starts.sort()
    res = []
    for interval in arr:
        end = interval[1]
        left = 0
        right = len(starts)-1
        index = -1
        while left <= right:
            mid = (left+right)//2
            if starts[mid][0] >= end:
                index = starts[mid][1]
                right = mid-1
            else:
                left = mid+1
        res.append(index)
    return res

arr =[[1,4],[2,3],[3,4]]
print(solution(arr))   
        
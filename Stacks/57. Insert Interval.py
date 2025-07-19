# 57. Insert Interval

def solution(arrs, intervals):
    arr = []
    inserted = False
    for interval in arrs:
        if not inserted and intervals[0] < interval[0]:
            arr.append(intervals)
            inserted = True
        arr.append(interval)

    if not inserted:
        arr.append(intervals)

    reslt = [arr[0]]
    for i in range(1,len(arr)):
        current = reslt[-1]
        if current[1] >= arr[i][0]:
            current[1] = max(current[1], arr[i][1])
        else:
            reslt.append(arr[i])

    return reslt,arr

def solution1(arr,interval):
    result = []
    i =0
    n = len(arr)
    while i < n and arr[i][1] < interval[0]:
        result.append(arr[i])
        i += 1

    while i < n and arr[i][0] <= interval[1]:
        interval[0] = min(arr[i][0], interval[0])
        interval[1] = max(arr[i][1],interval[1])
        i+=1
    result.append(interval)

    while i < n:
        result.append(arr[i])
        i += 1
    return result

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newInterval = [4,8]
print(solution1(intervals,newInterval))
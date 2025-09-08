# Non overlapping intervals

def solution(arr):
    arr.sort(key=lambda x : x[0])
    count = 0
    prev = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] <= prev:
            count +=1
            prev = min(prev, arr[i][1])
        else:
            prev = arr[i][1]
            
    return count
# find all good indices
from unittest import result


def solution1(arr,k):
    n = len(arr)
    prefix = [1] * n
    suffix = [1] * n

    # decreasing order prefix
    for i in range(1,n):
        if arr[i-1] >= arr[i]:
            prefix[i] = prefix[i-1]+1

    # increasing order suffix
    for i in range(n-2,-1,-1):
        if arr[i] <=  arr[i+1]:
            suffix[i] = suffix[i+1] + 1
    result = []
    for i in range(k, n-k):
        if prefix[i-1] >= k and suffix[i+1] >=  k:
            result.append(i)
    return result

nums = [2,1,1,1,3,4,1]
k = 2
print(solution1(arr=nums,k=k))

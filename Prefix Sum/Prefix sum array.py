# The task is to find the prefix sum array

def solution(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

arr = [10,20,30,40]
print(solution(arr))
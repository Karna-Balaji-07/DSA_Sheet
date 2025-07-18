# Increasing array

def solution(arr):
    result = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            result += arr[i-1] - arr[i]
            arr[i] = arr[i-1]
    return result

n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))
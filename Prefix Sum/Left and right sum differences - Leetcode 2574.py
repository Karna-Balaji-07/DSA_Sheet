# Left and right sum differences

def solution(arr):
    left = [0]*len(arr)
    right = [0] * len(arr)
    left[0] = 0
    for i in range(1,len(arr)):
        left[i] = arr[i-1] + left[i-1]
    for i in range(len(arr)-2,-1,-1):
        right[i] = arr[i+1] + right[i+1]
    for i in range(len(arr)):
        arr[i] = abs(left[i] - right[i])
    return arr

nums = [10,4,8,3]
print(solution(nums))
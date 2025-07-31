# 153. Find Minimum in Rotated Sorted Array


def solution(arr):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] > arr[high]:
            low = mid+1
        elif arr[mid] < arr[high]:
            high = mid
        
    return arr[low]

arr = [3,4,5,1,2]
print(solution(arr))
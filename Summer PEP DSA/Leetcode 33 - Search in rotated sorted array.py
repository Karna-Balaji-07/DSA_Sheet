# Search in rotated sorted array

def solution(arr,target):
    low = 0
    n = len(arr)
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[0]:
            if target >= arr[0] and target < arr[mid]:
                high = mid-1

            else:
                low = mid+1
        else:
            if target > arr[mid] and target <= arr[high]:
                low= mid+1
            else:
                high = mid-1
    return -1

arr = [4,5,6,7,1,2,3]
print(solution(arr,3))
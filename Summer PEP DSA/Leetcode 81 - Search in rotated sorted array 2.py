# Search in rotated sorted array II

def solution1(arr, target):
    if target in arr:
        return True
    return False

def solution2(arr, target):
    low = 0
    n = len(arr)
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return True

        if arr[mid] == arr[low] and arr[high] == arr[mid]:
            low += 1
            high -= 1
            continue

        if arr[low] <= arr[mid]:
            if target >= arr[low] and target < arr[mid]:
                high = mid-1
            else:
                low = mid+1

        else:
            if target > arr[mid] and target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return False

nums = [2,5,6,0,0,1,2]
target = 0

print(solution2(arr=nums,target=target))
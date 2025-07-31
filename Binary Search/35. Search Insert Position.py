# 35. Search Insert Position

def solution(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < target:
            low = mid+1
        elif arr[mid] >= target:
            high = mid-1
        
    return low

arr = [1,2,5,6]
print(solution(arr,7))
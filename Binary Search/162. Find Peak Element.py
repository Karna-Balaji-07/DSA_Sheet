# 162. Find Peak Element

def solution(arr):
    low = 0
    n = len(arr)
    high = n-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid
    
    return arr[low]

arr = [1,2,1,3,5,6,4]
print(solution(arr))
            
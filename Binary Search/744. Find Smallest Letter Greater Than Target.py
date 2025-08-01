# 744. Find Smallest Letter Greater Than Target

def solution(arr,target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low+high)//2
        if arr[mid] > target:
            high = mid
        else:
            low = mid+1        
    return arr[low % len(arr)]

arr = ["x","x","y","y"]
target = "z"
print(solution(arr,target))
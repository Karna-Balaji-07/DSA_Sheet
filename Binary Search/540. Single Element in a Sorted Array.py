# 540. Single Element in a Sorted Array

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    
    for key,values in dicts.items():
        if  values == 1:
            return key
    return -1
    
def solution2(arr):
    n = len(arr)
    left = 0
    right = n-1
    while left < right:
        mid = (left+right)//2
        if mid % 2 == 1:
            mid -=1
        if arr[mid] != arr[mid+1]:
            right = mid
        else:
            left = mid+2
    return arr[left]


nums = [1,1,2,3,3,4,4,8,8]
print(solution2(nums))
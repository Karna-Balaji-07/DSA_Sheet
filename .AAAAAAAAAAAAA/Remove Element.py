# Remove element

def solution1(arr, target):
    index = 0
    for i in range(len(arr)):
        if arr[i] != target:
            index+=1
    return index

def solution2(arr, target):
    left = 0
    n = len(arr)
    right = n-1
    while left <= right:
        if arr[left] == target and arr[right] != target:
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
        elif arr[right] == target:
            right -=1
        elif arr[left] != target:
            left +=1
    return left
nums = [0,1,2,2,3,0,4,2]; val = 2
print(solution1(nums,val))
print(solution2(nums,val))
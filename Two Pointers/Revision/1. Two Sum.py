# 1. Two Sum

# if array is unsorted
def solution1(arr,target):
    dicts = {}
    for i in range(len(arr)):
        curr = target - arr[i]
        if curr in dicts:
            return [i, dicts[curr]]
        dicts[arr[i]] = i
    return  []


# if array is sorted:
def solution2(arr, targer):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left <= right:
        curr = arr[left]+arr[right]
        if curr == target:
            return [left,right]
        elif curr > target:
            right -= 1
        elif curr < target:
            left +=1
    return []

arr = [2,7,11,15];target = 9
print(solution1(arr,target))
print(solution2(arr,target))
# Two sum

#unsorted
def solution1(arr, target):
    dicts = {}
    for index,value in enumerate(arr):
        diff = target - value
        if diff in dicts:
            return [index, dicts[diff]]
        else:
            dicts[value] = index
        
    return [-1,-1]

# sorted
def solution2(arr, target):
    left = 0
    right = len(arr)-1
    while left < right:
        sums = arr[left] + arr[right]
        if sums == target:
            return [left, right]
        elif sums > target:
            right -=1
        else:
            left += 1
    return [-1,-1]

nums = [2,7,11,15]; target = 9
print(solution1(nums,target))
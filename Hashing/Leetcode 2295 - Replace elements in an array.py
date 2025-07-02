# replace elements in an array

def solution1(arr,ops):
    dicts = {}
    for key,value in enumerate(arr):
        dicts[value] = key

    for target, value in ops:
        arr[dicts[target]] = value
        dicts[value] = dicts[target]
    return arr

nums = [1,2]
operations = [[1,3],[2,1],[3,2]]
print(solution1(nums, operations))
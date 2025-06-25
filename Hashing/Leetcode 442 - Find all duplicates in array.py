# find all duplicates in array

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    result = []
    for key, value in dicts.items():
        if value == 2:
            result.append(key)
    return result

def solution2(arr):
    result = []
    for i in range(len(arr)):
        index = abs(arr[i]) -1
        if arr[index] < 0:
            result.append(abs(arr[i]))
        else:
            arr[index] = -arr[index]

    return result



nums = [4,3,2,7,8,2,3,1]
print(solution2(nums))
# Product of array except self

def solution1(arr):
    result = [0] * len(arr)
    prod = 1
    zeros = 0
    index = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            index = i
        else:
            prod *= arr[i]  
    if zeros == 0:
        for i in range(len(arr)):
            result[i] = prod // arr[i]
    else:
        result[index] = prod
    return result

arr = [-1,1,0,-3,3]
print(solution1(arr))
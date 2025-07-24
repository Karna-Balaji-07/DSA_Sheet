# 2149. Rearrange Array Elements by Sign


def solution(arr):
    pos = 0
    neg = 1
    result = [0]*len(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            result[pos] = arr[i]
            pos += 2
        else:
            result[neg] = arr[i]
            neg += 2
        
    return result

nums = [3,1,-2,-5,2,-4]
print(solution(nums))
nums = [-1,1]
print(solution(nums))
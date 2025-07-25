# 238. Product of Array Except Self

def solution(arr):
    n = len(arr)
    prefix = [0]*n
    prod = 1
    zero = 0
    for i in range(n):
        if arr[i] != 0:
            prod *= arr[i]
        else:
            zero += 1
    
    for i in range(n):
        if zero > 1:
            prefix[i] = 0
        elif zero == 1:
            if arr[i] == 0:
                prefix[i] = prod
            else:
                prefix[i] = 0
        else:
            prefix[i] = prod // arr[i]
        
    return prefix


def solution1(arr):
    n = len(arr)
    prefix = [0]*n
    prod = 1
    count = 0
    for i in range(n):
        if arr[i] != 0:
            prod *= arr[i]
        else:
            count +=1
    for i in range(n):
        if count > 0:
            if arr[i] == 0:
                prefix[i] = prod
            else:
                prefix[i] = 0
        
        else:
            prefix[i] = prod // arr[i]
        
    return prefix

arr = nums =  [-1,1,0,-3,3]
print(solution(arr))
arr = nums =  [-1,1,0,-3,3]
print(solution1(arr))
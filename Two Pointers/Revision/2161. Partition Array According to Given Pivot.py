# 2161. Partition Array According to Given Pivot

def solution1(arr, pivot):
    less = []
    equal = []
    great = []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            great.append(i)
        else:
            equal.append(i)
            
    less.extend(equal)
    less.extend(great)
    return less

def solution2(arr,pivot):
    n = len(arr)
    left = 0
    right = n-1
    i = 0
    j = n-1
    result = [0]*n
    while i < n and j >= 0:
        if arr[i] < pivot:
            result[left] = arr[i]
            i += 1
            left +=1
        else:
            i +=1
        if arr[j] > pivot:
            result[right] = arr[j] 
            j -= 1
            right -= 1
        else:
            j-= 1
            
    while left <= right:
        result[left] = pivot
        left +=1
    
    return result

nums = [9,12,5,10,14,3,10];pivot = 10
print(solution2(nums,pivot))

# 2420. Find All Good Indices

def solution(arr,k):
    prefix = [1]*len(arr)
    suffix = [1]*len(arr)
    result = []
    for i in range(1,len(arr)):
        if arr[i-1] >= arr[i]:
            prefix[i] = prefix[i-1]+1
        
    for i in range(len(arr)-2,-1,-1):
        if arr[i] <= arr[i+1]:
            suffix[i] = suffix[i]+1
        
    for i in range(k,len(arr)-k):
        if prefix[i] >= k and suffix[i] <= k:
            result.append(i)
    return result

nums = [2,1,1,1,3,4,1]; k = 2
print(solution(nums,k))
# Find good days to rob the bank

def solution1(arr,time):
    n = len(arr)
    prefix = [0]*n
    suffix = [0]*n

    for i in range(1,n):
        if arr[i-1] >= arr[i]:
            prefix[i] = prefix[i-1] +1
    for i in range(n-2,-1,-1):
        if arr[i+1] >= arr[i]:
            suffix[i] = suffix[i+1]+1

    result = []
    for i in range(n):
        if prefix[i] >= time and suffix[i] >= time:
            result.append(i)
    return result

security = [5,3,3,3,5,6,2]
time = 2
print(solution1(security,time))
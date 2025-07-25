# 2100. Find Good Days to Rob the Bank

def solution(arr,time):
    prefix = [0]*len(arr)
    suffix = [0] * len(arr)
    result = []
    for i in range(1,len(arr)):
        if arr[i-1] >= arr[i]:
            prefix[i] = prefix[i-1] +1
    for i in range(len(arr)-2,-1,-1):
        if arr[i+1] >= arr[i]:
            suffix[i] = suffix[i+1]+1
        
    for i in range(len(arr)):
        if prefix[i] >= time and suffix[i] >= time:
            result.append(i)
    
    return result
security = [5,3,3,3,5,6,2]; time = 2
print(solution(security,time))
        
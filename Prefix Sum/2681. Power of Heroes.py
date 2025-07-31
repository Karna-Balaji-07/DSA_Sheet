# 2681. Power of Heroes


def subset(arr,result,i,ans):
    if  i == len(arr):
        ans.append(result[:])
        return
    
    result.append(arr[i])
    subset(arr, result,i+1,ans)
    result.pop() # Backtracking
    subset(arr,result,i+1,ans)
    

def solution(ans):
    sums = 0
    for i in ans:
        if len(i) != 0:
            maxi = max(i)
            mini = min(i)
            sums += maxi**2 * mini
    
    return sums

    
def solution2(arr):
    arr.sort()
    result = 1
    mod = 10**9+7
    for i in range(len(arr)):
        maxi = pow(2,i,mod)
        mini = pow(2,len(arr)-i-1,mod)
        term = (maxi*maxi)%mod
        term  =(term*mini) % mod
        result = (result*term ) % mod
    return result 

arr = [2,1,4]
print(solution2(arr))

arr = [2,1,4]
result = []
i = 0
ans = []
subset(arr, result,i,ans)
#sols = solution(ans)
#print(sols)
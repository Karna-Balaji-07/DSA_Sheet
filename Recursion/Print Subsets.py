# Print all the subsets of an array or string

def subset(arr,result,i,ans):
    if  i == len(arr):
        ans.add(result[:])
        return
    
    result.append(arr[i])
    subset(arr, result,i+1,ans)
    result.pop() # Backtracking
    subset(arr,result,i+1,ans)
    
arr = [1,2,3,4,5]
result = []
i = 0
ans = []
subset(arr, result,i,ans)
print(ans)
# permutations

def permutation(arr,index,ans):
    if index == len(arr):
        ans.append(arr[:])
        return
    
    for i in range(index,len(arr)):
        arr[index],arr[i] = arr[i],arr[index]
        permutation(arr,index+1,ans)
        arr[index],arr[i] = arr[i],arr[index]
    
arr = [1,2,3]
index = 0
ans = []
permutation(arr,index,ans)
print(ans)
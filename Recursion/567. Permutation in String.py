# 567. Permutation in String

def checkPermutations(arr,ans,index):
    if index == len(arr):
        ans.append(arr[:])
        return
    
    for i in range(index,len(arr)):
        arr[i],arr[index] = arr[index],arr[i]
        checkPermutations(arr,ans,index+1)
        arr[i],arr[index] = arr[index],arr[i]
    
s1 = "adc"; s2 = "dcda"
arr  = list(s1)
index = 0
ans = []
checkPermutations(arr,ans,index)
result = []
for i in range(len(ans)):
    s = "".join(ans[i])
    if s != s1:
        result.append("".join(ans[i]))

flag = False
for i in result:
    if i in s2:
        flag = True
print(flag)
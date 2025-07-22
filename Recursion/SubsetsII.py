# print all the unique subsets of an array containing duplicate elements

def subsets(arr,result,i,ans):
    if i == len(arr):
        ans.add(tuple(result[:]))
        return
    
    result.append(arr[i])
    subsets(arr,result,i+1,ans)
    result.pop()
    subsets(arr,result,i+1,ans)
    
def solution(arr,result,i,ans):
    if i == len(arr):
        ans.append(result[:])
        return
    
    result.append(arr[i])
    solution(arr,result,i+1,ans)
    result.pop()
    index = i+1
    while index < len(arr) and arr[index] == arr[index-1]:
        index +=1
    solution(arr,result,index,ans)
    
    
arr = [4,4,4,1,4]
arr.sort()
i = 0
result = []
ans  = set()
anss = []
subsets(arr,result,i,ans)
print(ans)
solution(arr,result,i,anss)
print(anss)
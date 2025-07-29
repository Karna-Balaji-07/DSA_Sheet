# 34. Find First and Last Position of Element in Sorted Array

def solution(arr,target,flag):
   first = 0
   last = len(arr)-1
   index = -1
   while last >= first:
        mid = (last+first)//2
        if arr[mid] == target:
            index = mid
            if flag:
                last = mid-1
            else:
                first = mid+1
        elif arr[mid] > target:
            last = mid-1
        else:
            first = mid+1
    
   return index

def main(arr,target):
    first =  solution(arr,target,True)
    last = solution(arr,target,False)
    result = [first,last]
    return result 
arr = [5,7,7,8,8,10]; target = 8
print(main(arr,target))
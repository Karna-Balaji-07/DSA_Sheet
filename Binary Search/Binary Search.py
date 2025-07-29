# Binary search

def iterative(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high -=1
        else:
            low +=1
        
    return -1

def recursive(arr,low,high,target):
    if low <= high:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursive(arr,low,mid-1,target)
        return recursive(arr,mid+1,high,target)
    return -1

arr = [1,3,5,7,9]
target = 3
print(iterative(arr,target))
print(recursive(arr,0,len(arr)-1,target))
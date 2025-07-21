# check if the given array is sorted in ascending or not

def isSorted(arr,n):
    if n <= 1:
        return True

    return arr[n-1] >= arr[n-2] and isSorted(arr,n-1)

arr = [1,2,3,8,5,6]
print(isSorted(arr,len(arr)))
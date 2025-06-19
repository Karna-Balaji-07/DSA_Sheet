# check if an array is sorted or not

def solution1(arr):
    for i in range(1,len(arr)):
        if arr[i-1] >  arr[i]:
            return False
    return True

arr = [1,2,3,4,5,6]
print(solution1(arr))
arr = [1,5,7,3,4,7,3,45]
print(solution1(arr))
# Move all zeros to the end of array

def solution1(arr):
    low = 0
    high = 1
    while high < len(arr):
        if arr[low] == 0 and arr[high] != 0:
            arr[low],arr[high] = arr[high],arr[low]
            high += 1
            low += 1
        if arr[low] != 0:
            low += 1
            if low == high:
                high += 1
        if arr[high] == 0:
            high += 1
    return arr

def solution(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    for i in range(index,len(arr)):
        arr[i] = 0

    return arr

arr = [1,2,0,3,0,1,0]
print(solution1(arr))
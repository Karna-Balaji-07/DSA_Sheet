# Sort a binary array

def solution1(arr):
    low = 0
    high = 1
    while  high <= len(arr):
        if arr[low] == 1 and arr[high] == 0:
            arr[low],arr[high] = arr[high],arr[low]
            high += 1
            low += 1
        if arr[low] == 0:
            low += 1
            if low == high:
                high += 1
        else:
            high += 1
    return arr

def solution2(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        if arr[low] == 1 and arr[high] == 0:
            arr[low],arr[high] = arr[high],arr[low]
            high -= 1
            low += 1
        if arr[low] == 0:
            low += 1
        if arr[high] == 1:
            high -= 1
    return arr


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(solution2(arr))
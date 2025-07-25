# Sort colors / sort 0s,1s,2s

def solution1(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 1:
            mid +=1
        elif arr[mid] == 0:
            arr[low], arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high],arr[mid]
            high -=1

    return arr
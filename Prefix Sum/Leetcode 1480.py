# Running sum of 1d array

def solution1(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i-1]
    return arr


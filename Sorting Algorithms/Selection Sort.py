# Selection sort

def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        idx = i
        for j in range(i+1,n):
            if arr[j] < arr[idx]:
                idx = j
        arr[idx],arr[i] = arr[i],arr[idx]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selectionsort(arr))
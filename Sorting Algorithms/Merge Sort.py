# Merge sort algorithm

def merge(arr, start, mid, end):
    left = mid - start +1
    right = end - mid
    lefts = arr[start : start + left]
    rights = arr[mid+1 : mid+1+right]
    i,j,k = 0,0,start

    while i < left and j < right:
        if lefts[i] < rights[j]:
            arr[k] = lefts[i]
            i += 1
        else:
            arr[k] = rights[j]
            j += 1
        k += 1

    while i < left:
        arr[k] = lefts[i]
        i += 1
        k += 1

    while j  <right:
        arr[k] = rights[j]
        j += 1
        k += 1


def mergesort(arr,start,end):
    if start >= end:
        return
    mid = (start+end)//2
    mergesort(arr,start,mid)
    mergesort(arr,mid+1,end)
    merge(arr,start,mid,end)



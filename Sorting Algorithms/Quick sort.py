# Quick sort algorithm

def partition(arr,start,end):
    pivot = arr[end] # pivot element
    i = start-1 # low pointer
    for j in range(start,end):
        if arr[j] <= pivot: # rearrange the elements around the pivot
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1] # place the pivot in the correct position
    return i+1 # return the pivot index

def quicksort(arr,start,end):
    if start < end:
        pivot = partition(arr,start,end)
        quicksort(arr,start,pivot-1)
        quicksort(arr,pivot+1,end)
    

# partition array according to given pivot

def solution1(arr, pivot):
    low = []
    high = []
    mid = []
    for i in arr:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            mid.append(i)
        else:
            high.append(i)

    arr = low + mid+high
    return arr

nums = [9,12,5,10,14,3,10]; pivot = 10
print(solution1(nums,pivot))

arr = [1,2,3,4,5,6,7]
print(arr[:-3])
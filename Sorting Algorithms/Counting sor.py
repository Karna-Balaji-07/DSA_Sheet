# counting sort algorithm

def countsort(arr):
    maxvalue = max(arr)
    count = [0] * (maxvalue+1)
    for i in arr:
        count[i] += 1

    for i in range(1,len(count)):
        count[i] += count[i-1]

    output = [0] * len(arr)

    for i in range(len(arr)-1,-1,-1):
        num = arr[i]
        output[count[num]-1] = num
        count[num] -= 1

    arr[:] = output
    return arr


arr = [1,4,17,2,9,22,12,35]
print(countsort(arr))
# rearrange array elements by sign

def solution1(arr):
    pos = 0
    neg = 1
    result =[0]*len(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            result[pos] = arr[i]
            pos += 2
        else:
            result[neg] = arr[i]
            neg += 2
    return result

arr = [3,1,-2,-5,2,-4]
print(solution1(arr))
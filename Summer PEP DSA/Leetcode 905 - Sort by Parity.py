# sort by parity

def solution1(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result  = even+odd
    return result

def solution2(arr):
    left = 0
    n = len(arr)
    right = n-1
    while left < right:
        if arr[left] % 2 != 0 and arr[right] % 2 == 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        elif arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 != 0:
            right -= 1
    return arr

arr = [3,1,5,4,2,7,4,8]
print(solution2(arr))
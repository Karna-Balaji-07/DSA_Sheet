
# sort array by parity II

def solution1(arr):
    even = 0
    odd = 1
    while odd < len(arr) and even < len(arr):
        if arr[even] % 2 != 0:
            arr[even],arr[odd] = arr[odd],arr[even]
            odd += 2
            even += 2
        elif arr[even] % 2 == 0:
            even += 2
        else:
            odd += 2
    return arr

arr = [4,2,5,7]
print(solution1(arr))

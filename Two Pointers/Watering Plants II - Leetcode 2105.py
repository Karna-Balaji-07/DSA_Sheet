# Water plants 2

def solution1(arr, a,b):
    A = a
    B = b
    result = 0
    left = 0
    n = len(arr)
    right   = n-1
    while left < right:
        if arr[left] > a:
            result += 1
            a = A
        a -= arr[left]
        left += 1

        if arr[right] > b:
            result += 1
            b = B
        b -= arr[right]
        right -= 1

    if left == right:
        if max(a,b) < arr[left]:
            result += 1
    return result



plants = [2,2,3,3]
capacityA = 3
capacityB = 4
print(solution1(plants,a=capacityA,b=capacityB))
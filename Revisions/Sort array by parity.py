# Sort array by parity

def solution1(arr):
    first = 0
    n = len(arr)
    last = n-1
    while first <= last:
        if arr[first] % 2 == 1 and arr[last] % 2 == 0:
            arr[first], arr[last] = arr[last],arr[first]
            first +=1
            last -=1
        elif arr[first] % 2 == 0:
            first += 1
        elif arr[last] % 2 ==1:
            last -= 1
    return arr

arr = [1,2,3,4,5,6]
print(solution1(arr))
    
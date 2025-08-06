# sort colors

def solution1(arr):
    zero = 0
    ones = 0
    twos = 0
    for i in arr:
        if i == 0:
            zero +=1
        elif i == 1:
            ones +=1
        else:
            twos +=1
        
    result = []

    one = [1]*ones
    two = [2]*twos
    zeros = [0] * zero
    result = zeros + one+two
    return result

def solution2(arr):
    first = 0
    last = len(arr)-1
    mid = 0
    while mid <= last:
        if arr[mid] == 0:
            arr[first],arr[mid] = arr[mid],arr[first]
            first +=1
            mid +=1
        elif arr[mid] ==1:
            mid +=1
        else:
            arr[mid],arr[last] = arr[last],arr[mid]
            last -=1
    return arr

arr = [0,0,0,1,2,0,1,2,2,1,0]
print(solution2(arr))
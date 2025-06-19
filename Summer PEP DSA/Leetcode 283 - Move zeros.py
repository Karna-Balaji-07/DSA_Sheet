#  move zeros

def solution1(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1
    for i in range(index,len(arr)):
        arr[i] = 0
    return arr

def solution2(arr):
    left = 0
    right = 1
    while right < len(arr) and left < len(arr):
        if arr[left] == 0 and arr[right] != 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right +=1
        elif arr[left] != 0:
            left += 1
            if left== right:
                right += 1
        elif arr[right] == 0:
            right += 1
    return arr

def solution3(arr):
    left = 0
    right = 0
    while right < len(arr):
        if arr[right] != 0:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
        right += 1
    return arr

arr =  [4,2,4,0,0,3,0,5,1,0]
print(solution3(arr))

# 75. Sort Colors

def solution1(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in arr:
        if i == 0:
            count0+=1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
        
    n= len(arr)
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count1+count0):
        arr[i] = 1
    for i in range(count0+count1,len(arr)):
        arr[i] = 2
    return arr

def solution2(arr):
    zero = []
    ones = []
    two = []
    for i in arr:
        if i == 0:
            zero.append(i)
        elif i == 1:
            ones.append(i)
        else:
            two.append(i)
    zero.extend(ones)
    zero.extend(two)
    return zero

# national flag algorithm
def solution3(arr):
    high = len(arr)-1
    low = 0
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid +=1
            low +=1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
        
    return arr

arr = [1, 0, 2, 1, 1 ,1 ,0]
print(solution1(arr))
print(solution2(arr))
print(solution3(arr))
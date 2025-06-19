# First missing positive
'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
'''

def solution1(arr):
    n = len(arr)
    current = 1
    for i in range(n):
        if current in arr:
            current += 1
        else:
            return current
    return current

def solution2(arr):
    n = len(arr)
    sets = set()
    for i in arr:
        if i > 0:
            sets.add(i)
    i = 1
    while True:
        if i not in arr:
            return i
        i += 1

def solution3(arr):
    n = len(arr)
    arr.append(0)
    for i in range(n):
        while 0 < arr[i] <= n and arr[i] != arr[arr[i]]:
            arr[i],arr[arr[i]] = arr[arr[i]],arr[i]

    for i in range(1,n+1):
        if arr[i] != i:
            return i
    return n+1

arr =  [-1,-2,-3,5,2]
print(solution2(arr))
# 3.	Remove Duplicates from Sorted Array 


def solution1(arr):
    return len(set(arr))

def solution2(arr):
    index = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            index +=1
    return index

arr = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,4,4]
print(solution2(arr))
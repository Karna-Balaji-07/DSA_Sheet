# Remove duplicates from sorted array

def solution(arr):
    index = 1
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            arr[index] = arr[i]
            index += 1
    return index

arr = nums = [0,0,1,1,1,2,2,3,3,4]
print(solution(arr))
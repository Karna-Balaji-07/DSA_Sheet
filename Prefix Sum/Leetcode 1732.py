# Find the highest altitide

def solution1(arr):
    result = [0]*(len(arr)+1)
    for i in range(1,len(arr)+1):
        result[i] = arr[i-1] + result[i-1]

    return max(result)

arr = gain = [-5,1,5,0,-7]
print(solution1(arr))

# sort the matrix

def solution1(arr):
    n = len(arr)
    m = len(arr[0])
    arrs = []
    for row in arr:
        for val in row:
            arrs.append(val)
    arrs.sort()
    index =0
    for i in range(n):
        for j in range(m):
            arr[i][j] = arrs[index]
            index += 1
    return arr

arr = [[5,4,7],[1,3,8],[2,9,6]]
print(solution1(arr))
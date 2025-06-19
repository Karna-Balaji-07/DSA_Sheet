# Sum of absolute differences in sorted array

def solution1(arr):
    result = []
    n = len(arr)
    for i in range(n):
        sums = 0
        for j in range(n):
            diff = abs(arr[i]-arr[j])
            print(f'difference : {diff}')
            sums += diff
            print(f'sums : {sums}')
        result.append(sums)
    return result

def solution2(arr):
    result = []
    sums = sum(arr)
    for i in arr:
        fix = sums - i +1

arr = [3,8,10]
print(solution1(arr))
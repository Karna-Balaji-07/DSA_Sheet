# Maximum sum of subarray of size k

def solution1(arr,k):
    maxs = float('-inf')
    n = len(arr)
    if n < k:
        return "Invalid"

    curr_sum = sum(arr[:k])
    result = curr_sum
    for i in range(k, n):
        result += arr[i] - arr[i-k]
        curr_sum= max(curr_sum, result)
    return curr_sum 

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(solution1(arr,k))
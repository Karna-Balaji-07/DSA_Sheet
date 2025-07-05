# 643. Maximum Average Subarray I

def solutions(arr,k):
    sums = sum(arr[:k])
    result = sums/k
    for i in range(k,len(arr)):
        sums  += arr[i] - arr[i-k]
        result = max(result, sums/k)
    return result

nums = [3,3,4,3,0]; k = 3
print(solutions(nums,k))


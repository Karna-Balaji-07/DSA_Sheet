# 2461. Maximum Sum of Distinct Subarrays With Length K

def solutions1(arr, k):
    n = len(arr)
    sums = 0
    result = 0
    s = set()
    pointer = 0
    for right in range(n):
        while arr[right] in s or right-pointer >= k :
            s.remove(arr[pointer])
            sums -= arr[pointer]
            pointer += 1

        s.add(arr[right])
        sums += arr[right]
        if (right-pointer +1)  == k:
            result = max(result,sums)

    return result


nums = [1,1,1,7,8,9]; k = 3
print(solutions1(nums, k))
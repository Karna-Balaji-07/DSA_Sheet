# Maximum sum of distinct subarrays of length k

def solution1(arr,k):
    n = len(arr)
    low = 0
    currsum = 0
    maxsum = 0
    s = set()
    for key in range(n):
        if arr[key] not in s:
            currsum += arr[key]
            s.add(arr[key])

            if key - low +1 == k:
                maxsum = max(maxsum,currsum)
                currsum -= arr[low]
                s.remove(arr[low])
                low += 1

        else:
            while arr[low] != arr[key]:
                currsum -= arr[low]
                s.remove(arr[low])
                low += 1
            low += 1
    return maxsum

nums = [1,5,4,2,9,9,9]; k = 3
print(solution1(nums,k))
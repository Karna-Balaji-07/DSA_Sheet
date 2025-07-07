# 209. Minimum Size Subarray Sum

def solutions1(arr,k):
    dicts = {}
    result = float('inf')
    currsum = 0
    left = 0
    for right in range(len(arr)):
        currsum += arr[right]
        while currsum >= k:
            result = min(result, right-left+1)
            currsum -= arr[left]
            left += 1

    return 0 if result == float('inf') else result



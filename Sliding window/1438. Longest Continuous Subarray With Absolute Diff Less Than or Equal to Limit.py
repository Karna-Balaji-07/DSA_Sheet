# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

def solutions1(arr, limit):
    left  = 0
    right = 0
    maxlen = 0
    while right < len(arr):
        minval = min(arr[left:right+1])
        maxval = max(arr[left:right+1])

        if abs(minval-maxval) <= limit:
            maxlen = max(maxlen, right-left+1)
            right +=1
        else:
            left += 1
            if left > right:
                right = left

    return maxlen

from collections import deque
def solutions2(arr,limit):
    result = 0
    mindeque = deque()
    maxdeque = deque()
    left = 0
    for right in range(len(arr)):
        while mindeque and arr[right] < mindeque[-1]:
            mindeque.pop()
        mindeque.append(arr[right])

        while maxdeque and arr[right] > maxdeque[-1]:
            maxdeque.pop()
        maxdeque.append(arr[right])

        while maxdeque[0] - mindeque[0] > limit:
            if arr[left] == maxdeque[0]:
                maxdeque.popleft()

            if arr[left] == mindeque[0]:
                mindeque.popleft()

            left += 1

        result = max(result, right-left+1)

    return result

nums = [8,2,4,7]; limit = 4

print(solutions1(nums,limit))


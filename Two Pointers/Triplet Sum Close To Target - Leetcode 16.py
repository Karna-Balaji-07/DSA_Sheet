# Triplet sum close to target

def triplet(arr, target):
    n = len(arr)
    arr.sort()
    result = 0
    mindiff = float('inf')
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            currsum = arr[left] + arr[right] + arr[i]
            if abs(currsum-target) < mindiff:
                mindiff = abs(currsum-target)
                result = currsum
            elif abs(currsum-target) == mindiff:
                result = max(result, currsum)

            if currsum > target:
                right -=1
            else:
                left += 1
    return result

arr = [-1, 2, 2, 4]
target= 4
print(triplet(arr,target))
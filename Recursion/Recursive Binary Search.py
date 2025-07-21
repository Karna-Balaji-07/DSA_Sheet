def binary(arr, start, end, target):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary(arr, mid + 1, end, target)
        return binary(arr, start, mid - 1, target)
    return -1

arr = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary(arr, 0, len(arr) - 1, target))  # Output: -1 (not found)

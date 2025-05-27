def water1(arr):
    left = 0
    right = len(arr)-1
    result = 0
    while left < right:
        water = min(arr[left], arr[right])*(right-left)
        result = max(result,water)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return result

arr = [2, 1, 8, 6, 4, 6, 5, 5]
print(water1(arr))
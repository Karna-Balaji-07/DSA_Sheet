# pair sum in a sorted and rotated array

def solution1(arr, target):
    index = 0
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            index = i
    arr = arr[index:] + arr[:index]
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == target:
            return True
        elif arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
    return False

arr = [7, 9, 1, 3, 5]; target = 6
print(solution1(arr, target))
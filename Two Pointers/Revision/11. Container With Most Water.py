# 11. Container With Most Water

def solution(arr):
    left = 0
    n = len(arr)
    right = n-1
    result = 0
    while right > left:
        area = min(arr[left],arr[right]) * (right-left)
        result = max(result, area)
        if arr[left] > arr[right]:
            right -=1
        else:
            left +=1
    return result
height = [1,8,6,2,5,4,8,3,7]
print(solution(height))
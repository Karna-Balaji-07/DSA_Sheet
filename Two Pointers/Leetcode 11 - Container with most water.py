# container with most water
from wsgiref.util import request_uri


def solution1(arr):
    left = 0
    right = len(arr)-1
    area = 0
    while left < right:
        lheight = max(arr[:left+1])
        rheight = max(arr[right-1:])
        height = min(lheight,rheight)
        area = max(area, (right-left)*height)
        if lheight < rheight:
            left += 1
        else:
            right -= 1
    return area

def solution2(arr):
    left = 0
    right = len(arr)-1
    result = 0
    while left < right:
        height = min(arr[left],arr[right])
        area = height * (right-left)
        result = max(area, result)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return result

height = height = [1,8,6,2,5,4,8,3,7]
print(solution2(height))


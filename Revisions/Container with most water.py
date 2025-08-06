# Container with most water

def solution(arr):
    left = 0
    result = 0
    right = len(arr)-1
    while left < right:
        area = (right-left) * min(arr[left],arr[right])
        result = max(result, area)
        
        if arr[left] > arr[right]:
            right -=1
        else:
            left +=1
    return result

arr = [1,8,6,2,5,4,8,3,7]
print(solution(arr))
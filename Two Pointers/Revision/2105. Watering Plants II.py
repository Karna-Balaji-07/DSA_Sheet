# 2105. Watering Plants II

def solution(arr, capacityA, capacityB):
    a = capacityA
    b = capacityB
    n = len(arr)
    result = 0
    left  = 0
    right = n-1
    while left < right:
        if arr[left] > a:
            result +=1
            a = capacityA
        a -= arr[left]
        left +=1
    
        if arr[right] > b:
            result +=1
            b = capacityB
        b -= arr[right]
        right -= 1
    
    if left == right:
        if max(a,b) < arr[left]:
            result +=1
    return result

plants = [2,2,3,3]; capacityA = 3; capacityB = 4
print(solution(plants, capacityA, capacityB))
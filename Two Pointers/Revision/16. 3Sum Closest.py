# 16. 3Sum Closest

def solution(arr,target):
    result = []
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        left = i+1
        right = n-1
        mindiff = float('inf')
        while left < right:
            curr = arr[i] + arr[left]+arr[right]
            mindiff = min(mindiff, abs(curr-target))
            result = curr
            if abs(curr-target) == target:
                result = max(curr, result)
            if curr > target:
                right -=1
            elif curr < target:
                left +=1
            
    return result


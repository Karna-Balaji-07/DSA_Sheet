# 3Sum closest 

def solution(arr, target):
    result = float('-inf')
    diff = float('inf')
    arr.sort()
    n = len(arr)
    for first in range(n-2):
        second = first+1
        third = n-1
        while second < third:
            sums = arr[first] + arr[second] + arr[third]
            if abs(sums-target) == target:
                result = max(diff, sums)
            elif abs(sums-target) < diff:
                diff = abs(sums-target)
                result = diff
            if sums > target:
                right -=1
            else:
                left +=1
    return result       
                
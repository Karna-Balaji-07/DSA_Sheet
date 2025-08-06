# Merge sorted array

def solution(arr1,arr2,m,n):
    left = m-1
    right = n-1
    k = m+n-1
    while left >= 0 and right >= 0:
        if arr1[left] > arr2[right]:
            arr1[k] = arr2[left]
            left -= 1
        else:
            arr1[k] = arr1[right]
            right -=1
        
        k -=1
    
    if right >= 0:
        arr1[k] = arr2[right]
        right -=1
        k -= 1
    
        
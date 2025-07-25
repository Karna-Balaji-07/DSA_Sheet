# trapping rain water

def solution1(arr):
    left = 1
    right = len(arr)-2
    lmax = arr[left-1]
    rmax = arr[right+1]
    result = 0
    while left <= right:
        if rmax <= lmax:
            result += max(0,rmax-arr[right])
            rmax = max(rmax, arr[right])
            right -= 1
        else:
            result += max(0, lmax-arr[left])
            lmax = max(lmax, arr[left])
            left +=1
        
    return result

arr = [2, 1, 5, 3, 1, 0, 4]
print(solution1(arr))
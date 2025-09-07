def twopointers(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        sums = arr[left] + arr[right]
        if sums == target:
            return [left,right]
        elif sums > target:
            right -=1
        else:
            left +=1
    
    return -1


# Koko eating bananas

def time(arr,mid,h):
    hours = 0
    for i in range(len(arr)):
        hours += arr[i] // mid
        if arr[i] % mid != 0:
            hours += 1

    return hours <= h

def solution(arr,h):
    low = 1
    result = max(arr)
    high = max(arr)
    while low <= high:
        mid = (low+high) //2

        if time(arr,mid,h) == True:
            high = mid-1
            result = mid
        else:
            low  = mid+1
    return result

piles = [3,6,7,11]; h = 8
print(solution(piles,h))
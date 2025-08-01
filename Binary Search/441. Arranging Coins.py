# 441. Arranging Coins

def solution(n):
    low = 0
    high = n
    while low <= high:
        mid = (low+high) //2
        current = mid * (mid+1) //2
        if current == n:
            return mid
        elif current < n:
            low = mid+1
        else:
            high = mid-1
    return high

n = 8
print(solution(n))
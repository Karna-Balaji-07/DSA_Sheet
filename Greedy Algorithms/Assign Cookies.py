# Assign Cookies

def solution(greed, size):
    n = len(greed)
    m = len(size)
    greed.sort()
    size.sort()
    left = 0
    right = 0
    while left < m and right < n:
        if size[left] >= greed[right]:
            right +=1
        left +=1
    
    return right
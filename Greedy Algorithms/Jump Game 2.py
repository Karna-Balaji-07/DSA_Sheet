# Jump game 2

def solution(arr):
    last = 0
    jumps = 0
    maxi = 0
    for i in range(len(arr)-1):
        maxi = max(maxi, i+arr[i])
        if i == last:
            jumps += 1
            last = maxi
            
    return jumps
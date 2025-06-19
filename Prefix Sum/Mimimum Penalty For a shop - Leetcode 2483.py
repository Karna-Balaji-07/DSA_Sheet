# Minimum penalty for a shop

def solution(s):
    n = len(s)
    prefix = [0]* (n+1)
    suffix = [0]*(n+1)
    prefix[0] = 0
    suffix[0] = 0
    for i in range(1, n+1):
        if s[i] == 'N':
            prefix[i] = prefix[i-1]+1
        else:
            prefix[i] = prefix[i-1]

    for i in range(n-1,-1,-1):
        if s[i] == 'Y':
            suffix[i] = suffix[i+1]+1
        else:
            suffix[i] = suffix[i+1]
    penalty = float('inf')
    minhour = float('inf')
    for i in range(n+1):
        curr = prefix[i] +  suffix[i]
        if curr < penalty:
            penalty = curr
            minhour = i
    return minhour

def solution1(arr):
    n = len(arr)
    penalty = arr.count('Y')
    minhour = 0
    minpen = penalty
    for i in range(n):
        if arr[i] == "Y":
            penalty -= 1
        else:
            penalty += 1
        if penalty < minpen:
            minpen = penalty
            minhour = i+1
    return minhour

s = "YYYY"
print(solution(s))

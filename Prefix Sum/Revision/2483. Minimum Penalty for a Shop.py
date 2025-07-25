# 2483. Minimum Penalty for a Shop

def solution(s):
    open = [0]*(len(s)+1)
    close = [0]*(len(s)+1)
    n = len(s)
    for i in range(1,n+1):
        if s[i-1] == 'N':
            open[i] = open[i-1]+1
        else:
            open[i] = open[i-1]
    
    for i in range(n-1,-1,-1):
        if s[i] == 'Y':
            close[i] = close[i+1]+1
        else:
            close[i] = close[i+1]
        
    minhour = 0
    penalty = float('inf')
    for i in range(n+1):
        diff = open[i] + close[i]
        if diff < penalty:
            penalty = diff
            minhour = i
            
            
    return minhour

customers = "YYNY"
print(solution(customers))
# 50. Pow(x, n)

def solution(x,n):
    if n == 0:
        return 1
    if n < 0:
        return solution(1/x,-n)
    return solution(x,n-1)*x if n % 2 else solution(x*x,n/2)

x = 2.000
n = 10
result = solution(x,n)
print(result)
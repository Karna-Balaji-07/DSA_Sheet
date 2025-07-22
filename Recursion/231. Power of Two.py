# 231. Power of Two

def solution(n):
    if n <= 0:
        return False
    if n ==1:
        return True
    
    return (n % 2 == 0 and solution(n//2))

def solution2(n):
    if n <=0:
        return False

    while n > 1:
        n //=2
    if n == 1:
        return True
    return False


n = 18
result = solution(n)
print(result)
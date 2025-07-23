# Trailing zeros
# Your task is to calculate the number of trailing zeros in the factorial n!.
def solution1(n):
    def facts(n):
        if n <= 1:
            return 1
        return n*facts(n-1)
    s = str(facts(n))
    count = 0
    for i in s[::-1]:
        if i != '0':
            return count
        count += 1
    
    return count

def solution(n):
    count = 0
    while n >= 5:
        n //= 5
        count +=n
    return count

n = int(input())
print(solution(n))
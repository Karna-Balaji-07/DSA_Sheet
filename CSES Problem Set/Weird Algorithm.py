# Weird Algorithm

'''
Consider an algorithm that takes as input a positive integer n.
If n is even, the algorithm divides it by two, and if n is odd,
the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one.

'''

def solution(n):
    result=[]
    result.append(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n % 2 != 0:
            n = n*3 +1
        result.append(n)
    return result
n = int(input())
print(' '.join(map(str, solution(n))))
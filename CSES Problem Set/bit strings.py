# bit strings
'''
Your task is to calculate the number of bit strings of length n.
For example, if n=3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
'''
def solution(n):
    mod = 10**9+7
    return (2**n) % mod 

n = int(input())
print(solution(n))

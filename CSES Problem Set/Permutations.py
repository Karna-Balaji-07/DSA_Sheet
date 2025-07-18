# Permutations

def solution1(n):
    odd = []
    even = []
    if n == 3 or n == 2:
        return ['NO SOLUTION']
    for i in range(1,n+1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.extend(odd)
    return even

n = int(input())
print(' '.join(map(str, solution1(n))))
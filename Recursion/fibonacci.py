# fibonacci series

def solution1(n):
    if n <= 1:
        return n
    
    return solution1(n-1) + solution1(n-2)

def printsols(n):
    for i in range(n):
        print(solution1(i),end=" ")

n = 5
print(printsols(n))
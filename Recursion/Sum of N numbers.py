# Sum of n numbers using recursion

def recursion(n):
    if n == 1:
        return 1 
    return n + recursion(n-1)

n = 4
print(recursion(4))
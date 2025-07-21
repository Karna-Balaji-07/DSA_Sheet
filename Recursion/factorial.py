"""
Factorial of a number    
    """
    
def factorial(n):# -> Any | Literal[1]:# -> Any | Literal[1]:
    if n == 0:
        return 1
    return n * factorial(n-1)

n = 4
print(factorial(n))
"""_summary_
    creating a function that prints number from n to 1
"""
def recursion(n) -> None:
    if n == 1:
        print(n)
        return
    print(n,end=" ")
    recursion(n-1)

n = 5
recursion(n)
print("test")
    

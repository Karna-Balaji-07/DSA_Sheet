# Missing number

def solutions(n,arr):
    total = n * (n+1)//2
    sums = sum(arr)
    return total - sums

n = int(input())
arr = list(map(int, input().split()))

print(solutions(n,arr))
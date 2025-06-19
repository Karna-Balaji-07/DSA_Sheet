# Square root of x using binary search

def search(n):
    low = 1
    high = n
    result = 1
    while low <= high:
        mid = (high+low) // 2
        if mid*mid <= n:
            result = mid
            low = mid+1
        else:
            high = mid-1

    return result

n = 100
print(search(n))
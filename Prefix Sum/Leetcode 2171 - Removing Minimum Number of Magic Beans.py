# 2171. Removing Minimum Number of Magic Beans

def solutions(arr):
    arr.sort()
    total = sum(arr)
    n = len(arr)
    result = float('inf')
    for i in range(len(arr)):
        result = min(result, total - (n-i)*arr[i])
    return result

beans = [4,1,6,5]
print(solutions(beans))
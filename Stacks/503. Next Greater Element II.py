# 503. Next Greater Element II

def solutions(arr):
    maxi = max(arr)
    stack = []
    result = [-1]*len(arr)
    for i in range(2 * len(arr)-1,-1,-1):
        current = arr[i%len(arr)]
        while stack and stack[-1] < current:
            stack.pop()
        if i < len(arr):
            if stack and stack[-1] > current:
                result[i] = stack[-1]
        stack.append(current)

    if arr[-1] == maxi:
        return result

    else:
        result[len(arr)-1] = maxi
        return result

nums = [5,4,3,2,1]
print(solutions(nums))
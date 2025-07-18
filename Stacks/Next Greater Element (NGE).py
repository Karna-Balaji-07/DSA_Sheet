# Next Greater Element (NGE)

def solution(arr):
    stack = []
    result = [-1]*len(arr)
    n = len(arr)
    for i in range(n-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack and arr[i] < stack[-1]:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result


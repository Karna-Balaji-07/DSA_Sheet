# the stock span problem

def solution(arr):
    stack = []
    n = len(arr)
    result = [0]*n
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if not stack:
            result[i] = i+1
        else:
            result[i] = i - stack[-1]
        stack.append(i)

    return result
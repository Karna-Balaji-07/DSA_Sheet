# The next greater element

def solution1(arr):
    stack = []
    result = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)

    return result


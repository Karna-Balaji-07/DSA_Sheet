# Maximum product of indexes of next greater on left and right

def lefts(arr):
    stack = []
    left = [0]*len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack :
            left[i] = stack[-1]+1

        stack.append(i)

    return left

def rights(arr):
    stack = []
    right = [0] * len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        if stack :
            right[i] = stack[-1]+1
        stack.append(i)
    return right

def solution(arr):
    left = lefts(arr)
    right = rights(arr)
    for i in range(len(left)):
        left[i] *= right[i]
    return max(left)

arr =[5, 4, 3, 4, 5]
print(solution(arr))
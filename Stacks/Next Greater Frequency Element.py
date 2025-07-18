# Next Greater Frequency Element

def solution(arr):
    stack = []
    result = [-1]*len(arr)
    dicts= {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1

    for i in range(len(arr)-1,-1,-1):
        while stack and dicts[stack[-1]] <= dicts[arr[i]]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result, dicts


arr = [2, 6, 4, 2, 2, 10, 7 ,5]
print(solution(arr))
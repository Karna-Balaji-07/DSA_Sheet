# Daily temperatures

def solution1(arr):
    stack = []
    daily = [0] * len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            daily[stack[-1]] = i - stack[-1]
            stack.pop(-1)

        stack.append(i)
    return daily

temperatures = [73,74,75,71,69,72,76,73]
print(solution1(temperatures))
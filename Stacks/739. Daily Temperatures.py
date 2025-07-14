# 739. Daily Temperatures

def solutions(temp):
    result = [0]*len(temp)
    stack = []
    for i in range(len(temp)):
        while stack and temp[stack[-1]] < temp[i]:
            result[stack[-1]] = i - stack[-1]
            stack.pop(-1)
        stack.append(i)
    return result

temperatures = [73,74,75,71,69,72,76,73]
print(solutions(temperatures))
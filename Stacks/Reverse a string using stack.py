# reverse a string using stack

def solution(s):
    stack = []
    result = ""
    for i in s:
        stack.append(i)
    while stack:
        result += stack.pop()
    return result

s = "WElcome"
print(solution(s))
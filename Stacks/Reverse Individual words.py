# reverse individual words

def solution(s):
    result = ""
    stack = []
    for i in range(len(s)):
        if s[i] != ' ':
            stack.append(s[i])
        elif s[i] == ' ' :
            while stack:
                a =  stack.pop()
                result += a
            result += " "
    while stack:
        a = stack.pop()
        result += a
    return result
s = "Hello world"
print(solution(s))
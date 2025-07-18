# Postfix to prefix conversion

def operator(i):
    if i in ['+','-','*','/','^']:
        return True
    return False

def solution(s):
    n = len(s)
    stack = []
    result = ""
    for i in range(n):
        if not operator(s[i]):
            stack.append(s[i])
        else:
            s1 = stack[-1]
            stack.pop()
            s2 = stack[-1]
            stack.pop()
            strings = s[i] + s2+s1
            result += strings
            stack.append(strings)
    return stack.pop()

s = "AB+CD-*"
print(solution(s))
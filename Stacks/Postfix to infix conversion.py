# Postfix to infix conversion

def operator(i):
    if i in ['+','-','*','/','^']:
        return True
    return False

def solution(s):
    stack = []
    result = ""
    for i in range(len(s)):
        if not operator(s[i]):
            stack.append(s[i])
        else:
            s1 = stack[-1]
            stack.pop()
            s2 = stack[-1]
            stack.pop()
            strings = "("+ s2+ s[i]+s1+")"
            result += strings
            stack.append(strings)
    return stack.pop()

s = "abc++"
print(solution(s))
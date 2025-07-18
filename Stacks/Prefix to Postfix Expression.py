# Prefix to Postfix conversion

def operator(i):
    if i in ['+','-','*','/','^']:
        return True
    return False

def solution(s):
    stack = []
    result = ""
    i = len(s)-1
    while i >= 0:
        if not operator(s[i]):
            stack.append(s[i])
            i -= 1
        else:
            strings = stack.pop()+stack.pop()+ s[i]
            result += strings
            stack.append(strings)
            i -=1

    return stack.pop()

s = "*+AB-CD"
print(solution(s))
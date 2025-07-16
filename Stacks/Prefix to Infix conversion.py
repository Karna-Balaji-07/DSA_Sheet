# Prefix to infix conversion

def operators(i):
    if i in ('+','-','*','/','^',')','('):
        return True
    return False

def solution(s):
    stack = []
    result = ""
    i = len(s)-1
    while i >= 0:
        if not operators(s[i]):
            stack.append(s[i])
            i -= 1
        else:
            string = '('+stack.pop() +s[i] + stack.pop()+')'
            stack.append(string)
            result += string
            i -= 1
    return stack.pop()

s = "*-A/BC-/AKL"
print(solution(s))

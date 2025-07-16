# Infix exp to postfix

def precedence(i):
    if i == '^':
        return 3
    elif i in ('/','*'):
        return 2
    elif i in ('+','-'):
        return 1
    else:
        return -1

def solutions(s):
    stack = []
    result = []
    for i in s:
        if i.isalnum():
            result += i

        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack and stack[-1] == '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(i) <= precedence(stack[-1]):
                result += stack.pop()
            stack.append(i)

    while stack:
        result += stack.pop()
    return result



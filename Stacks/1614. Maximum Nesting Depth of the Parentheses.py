# 1614. Maximum Nesting Depth of the Parentheses

def solutions1(s):
    stack = []
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '(':
            stack.append(s[i])

        elif s[i] not in ['(',')']:
            continue
        else:
            count = max(count, len(stack))
            if stack and stack[-1] == '(' and s[i] == ')':
                stack.pop()


    return count

s = "(1)+((2))+(((3)))"
print(solutions1(s))

# 856. Score of Parentheses

def solutions1(s):
    count = 0
    stack = []
    for i in s:
        if i == '(':
            stack.append(count)
            count = 0
        else:
            count += stack.pop() + max(count,1)
    return count

s = "(()(()))"
print(solutions1(s))

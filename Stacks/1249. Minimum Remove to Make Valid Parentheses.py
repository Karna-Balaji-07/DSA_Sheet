# 1249. Minimum Remove to Make Valid Parentheses

def solutions1(s):
    n = len(s)
    arr = list(s)
    stack = []
    invalid= set()
    for key, value in enumerate(s):
        if value  == '(':
            stack.append(key)
        elif value == ')':
            if stack:
                stack.pop()
            else:
                invalid.add(key)
    invalid.update(stack)
    result = []
    for key, value in enumerate(arr):
        if key not in invalid:
            result.append(value)
    return "".join(result)

s = "lee(t(c)o)de)"
print(solutions1(s))
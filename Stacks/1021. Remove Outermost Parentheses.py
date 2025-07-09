# 1021. Remove Outermost Parentheses

def solutions1(s):
    n = len(s)
    stack =[]
    result = []
    strings = ""
    for i in range(n):
        if s[i] == '(':
            stack.append(s[i])
            strings += s[i]
        else:
            stack.pop()
            strings += s[i]
            if not stack:
                result.append(strings[1:-1])

                strings = ""

    return "".join(result)

def solutions2(s):
    count = 0
    result = []
    for i in range(len(s)):
        if s[i] == '(':
            if count > 0:
                result.append(s[i])
            count +=1
        else:
            count -= 1
            if count > 0:
                result.append(s[i])

    return ''.join(result)



s = "(()())(())(()(()))"
print(solutions2(s))

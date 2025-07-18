# Valid parentheses in expression

def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] in ('{','[','('):
            stack.append(s[i])
        else:
            if stack and ((stack[-1] == '(' and s[i] == ')') or (stack[-1] == '[' and s[i] == ']') or (stack[-1] =='{' and s[i]=='}')):
                stack.pop()
            else:
                return False
    return not stack

s = "{([])}"
print(solution(s))
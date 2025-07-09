# 921. Minimum Add to Make Parentheses Valid

def solutions1(s):
    stack = []
    arr = list(s)

    while arr:
        if arr[0] == '(':
            stack.append(arr[0])
            arr.pop(0)
        else:
            if stack:
                stack.pop()
                arr.pop(0)
            else:
                break

    if stack:
        return len(stack)
    elif arr:
        return len(arr)


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        arr = list(s)
        count = 0

        for chars in arr:
            if chars == '(':
                stack.append(chars)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count

s = "((("
print(solutions1(s))

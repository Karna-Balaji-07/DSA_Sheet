# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
from typing import List
def solutions(s):
    result = [0]*len(s)
    depth = 0
    for index, value in enumerate(s):
        if value == '(':
            result[index] = depth & 1
            depth += 1
        else:
            depth -= 1
            result[index] = depth & 1

    return result

s = "()(())()"
print(solutions(s))
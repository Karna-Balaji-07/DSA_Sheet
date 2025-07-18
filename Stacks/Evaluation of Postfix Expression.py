# Evaluation of Postfix Expression
import math
def operator(i):
    if i in ['+','-','*','/','^']:
        return True
    return False

def solution(arr):
    stack = []
    result = ""
    for i in range(len(arr)):
        if arr[i].lstrip('-').isdigit():
            stack.append(int(arr[i]))
        else:
            val1 = stack.pop()
            val2 =stack.pop()
            if arr[i] == '+':
                stack.append(val1+val2)
            elif arr[i] == '-':
                stack.append(val2-val1)
            elif arr[i] == '*':
                stack.append(val1 * val2)
            elif arr[i] == '/':
                stack.append(math.trunc(val2/val1))

    return stack.pop()

arr = ["2", "3", "1", "*", "+", "9", "-"]
print(solution(arr))
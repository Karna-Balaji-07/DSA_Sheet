# 456. 132 Pattern

def solutions(arr):
    third = float('-inf')
    stack = []
    for i in reversed(arr):
        if i < third:
            return True
        while stack and stack[-1] < i:
            third = stack.pop()
        stack.append(i)
    return False

nums = [1,2,3,4]
print(solutions(nums))
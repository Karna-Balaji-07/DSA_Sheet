def reverse_stack(stack):
    result = []
    if len(stack) == 0:
        return result
    result.append(stack[-1])
    return reverse_stack(stack.pop())
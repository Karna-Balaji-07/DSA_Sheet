# 1475. Final Prices With a Special Discount in a Shop

def solutions1(arr):
    stack = []
    result = []*len(arr)
    for i in range(len(arr)-1,-1,-1):
        current = arr[i]
        while stack and stack[-1] > arr[i]:
            stack.pop()

        discount = stack[-1] if stack else 0
        result.append(current-discount)
        stack.append(current)
    return result[::-1]






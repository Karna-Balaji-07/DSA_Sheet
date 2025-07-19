# 735. Asteroid Collision

def solution(arr):
    stack = []
    for i in arr:
        if i > 0:
            stack.append(i)
        else:
            while stack and 0 < stack[-1] < -i:
                stack.pop()
            if stack and stack[-1] == -i:
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(i)
    return stack

asteroids = [5, 5, 2, 1, 1, -2]
print(solution(asteroids))
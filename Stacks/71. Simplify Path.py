# 71. Simplify Path

def solution(path):
    parts = [p for p in path.split('/') if p]
    string = ""
    stack = []
    for i in parts:
        if  i == '..':
            if stack:
                stack.pop()
        elif i == '.':
            continue
        else:
            stack.append(i)
    if stack:
        for i in stack:
            string += "/"+i

    else:
        string = "/"
    return string

path = "/home/user/Documents/../Pictures"
print(solution(path))
path = "/home//foo/"
print(solution(path))
path = "/home/"
print(solution(path))
path = "/.../a/../b/c/../d/./"
print(solution(path))
path = "/../"
print(solution(path))
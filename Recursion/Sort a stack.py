# Sort a stack 

def solution1(s):
    s.sort()
    return s

def solution2(s):
    stack = []
    while s:
        mini = min(s)
        s.remove(mini)
        stack.append(mini)
    return stack


def solution3(s):
    
    def sorts(s,x):
        if not s or x > s[-1]:
            s.append(x)
            return s
        temp = s.pop()
        sorts(s,x)
        s.append(temp)
    
    if s:
        x= s.pop()
        solution3(s)
        sorts(s,x)
arr = [11,2,32,41,3]
solution3(arr)
print(arr)
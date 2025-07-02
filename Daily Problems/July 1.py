# Find the original typed string I

def solution1(s):
    count = len(s)
    n = len(s)
    for i in range(1,n):
        if s[i] != s[i-1]:
            count -= 1
    return count

word = "abbcccc"
print(solution1(word))
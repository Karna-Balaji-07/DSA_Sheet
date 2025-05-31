# Minimmum length of strings after deleting similar ends

def solution(s):
    left =0
    n = len(s)
    right = n-1
    while left <= right and s[left] == s[right]:
        char = s[left]
        while left <= right and s[left] == char:
            left += 1
        while left <= right and s[right] == char:
            right  -= 1

    return right - left +1

s = "ca"
print(solution(s))
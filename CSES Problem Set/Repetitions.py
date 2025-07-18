# Repetitions

def solution(s):
    end =0
    start = 0
    maxlen = float('-inf')
    while start < len(s):
        start = end
        count = 0
        while end < len(s) and s[start] == s[end]:
            count += 1
            end += 1
        maxlen = max(maxlen, count)
    return maxlen

s = input()
print(solution(s))

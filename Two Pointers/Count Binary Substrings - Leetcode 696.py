# Count binary substrings

def solution(s):
    i = 0
    n = len(s)
    result = 0
    while i < n:
        c0 = 0
        c1 = 0
        if s[i] == '0':
            while i < n and s[i] == '0':
                c0 += 1
                i += 1

            j = i
            while j < n and s[j] == '1':
                c1 += 1
                j += 1
        else:
            while i < n and s[i] == '1':
                c1 += 1
                i += 1
            j = i
            while j < n and s[j] == '0':
                c0 += 1
                j += 1

        result += min(c0,c1)

    return result


s = "00110011"
print(solution(s))



# reverse a string with spaces intact

def solutio1(s):
    index = []
    chars = []
    for i in range(len(s)):
        if s[i] == ' ':
            index.append(i)
        else:
            chars.append(s[i])
    k = 0
    result = []
    chars = chars[::-1]
    for i in range(len(s)):
        if i in index:
            result.append(" ")
        else:
            result.append(chars[k])
            k += 1

    return index,"".join(result)

def solution2(a):
    left = 0
    s = list(a)
    k = list(a)
    right = len(a)-1
    while left < right:
        if s[left] == ' ':
            left += 1
            continue
        elif s[right] == ' ':
            right -= 1
            continue

        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s),k

s = S = "Help others"
print(solution2(s))
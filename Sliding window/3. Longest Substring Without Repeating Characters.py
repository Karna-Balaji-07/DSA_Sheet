# 3. Longest Substring Without Repeating Characters

def solutions1(s):
    left = 0
    right = 0
    count = 0
    arr = ""
    result = 0
    if len(s) == 1:
        return 1
    while right < len(s):
        if s[right] not in arr:
            arr += s[right]
            count += 1
            right += 1
        elif s[right] in arr:
            result = max(result, count)
            left += 1
            right = left
            arr = ""
            count = 0
    return result

def solutions2(s):
    sets = set()
    left = 0
    maxlen = 0
    for right in range(len(s)):
        while s[right] in sets:
            sets.remove(s[left])
            left += 1
        sets.add(s[right])
        maxlen = max(maxlen, right-left+1)
    return maxlen

s = s = " "
print(solutions1(s))
print(len(" "))
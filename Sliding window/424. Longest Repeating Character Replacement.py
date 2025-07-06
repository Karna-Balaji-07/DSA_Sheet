# 424. Longest Repeating Character Replacement



def soutions(s,k):
    left = 0
    dicts = {}
    maxlen = 0
    result = 0
    for right in range(len(s)):
        dicts[s[right]] = dicts.get(s[right],0)+1
        maxlen = max(maxlen, dicts[s[right]])
        if right-left +1 - maxlen > k:
            dicts[s[right]] -=1
            left += 1
        result = max(result, right-left+1)
    return result

s = "ABAB"
K = 2
print(soutions(s,K))

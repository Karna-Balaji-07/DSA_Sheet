# 1456. Maximum Number of Vowels in a Substring of Given Length

def solutions1(s,k):
    dicts = {}
    count = 0
    maxcount = 0
    vowels = ['a','e','i','o','u']
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        if i >= k:
            if s[i-k] in vowels:
                count -= 1
        maxcount = max(count, maxcount)
    return  maxcount




s = "abciiidef"; k = 3
print(solutions1(s,k))
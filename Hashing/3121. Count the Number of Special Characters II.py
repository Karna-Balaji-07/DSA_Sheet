# 3121. Count the Number of Special Characters II

def solutions1(words):
    lower ={}
    upper  = {}
    for key, value in enumerate(words):
        if value.islower():
            if value not in lower:
                lower[value] = []
            lower[value].append(key)
        elif value.isupper():
            if value not in upper:
                upper[value] = key
    uppers = dict(sorted(upper.items()))
    lowers = dict(sorted(lower.items()))

    count = 0
    for key, value in uppers.items():
        low = key.lower()
        if low in lowers:
            if all(index < value for index in lower[low]):
                count +=1
    return count

def solution2(words):
    lower = [False]*26
    upper = [False] * 26
    for i in word:
        if i.islower():
            lower[ord(i)-ord('a')] = True
        elif i.isupper():
            upper[ord(i)-ord('A')] = True

    return sum([a and b for a, b in zip(lower, upper)])

word =  "cCceDC"
print(solutions1(word))
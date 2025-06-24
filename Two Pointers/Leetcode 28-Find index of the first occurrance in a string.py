# FInd index of the first occurrance in a string

def solution1(s1,s2):
    first = len(s1)
    second = len(s2)
    for i in range(first-second+1):
        if s1[i:i+second] == s2:
            return i
    return -1

s1 = "leetcode"
s2 = "leeto"
print(solution1(s1,s2))
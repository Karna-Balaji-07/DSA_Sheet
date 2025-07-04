# 438. Find All Anagrams in a String

def solutions1(s,k):
    l = len(k)
    result = []
    for i in range(len(s)-l+1):
        substr = s[i:i+l]
        if len(substr) == len(k) and sorted(k) == sorted(substr):
            result.append(i)
    return result

def solutions2(s,k):
    freq1 = [0]*26
    freq2 = [0]*26
    for i in k:
        freq1[ord(i)-ord('a')] += 1
    result = []
    for i in range(len(s)):
        freq2[ord(s[i])-ord('a')] += 1
        if i >= len(k):
            freq2[ord(s[i-len(k)])-ord('a')] -= 1
        if freq1 == freq2:
            result.append(i-len(k)+1)
    return result



s = "cbaebabacd"; p = "abc"
print(solutions2(s,p))
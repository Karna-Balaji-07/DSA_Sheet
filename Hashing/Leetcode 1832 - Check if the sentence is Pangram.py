# Check if the sentence is pangram

def solution1(s):
    dicts = {}
    for i in s:
        dicts[i] = dicts.get(i,0)+1
    count = 0
    for key in dicts.keys():
        count += 1
    if count < 26:
        return False
    return True

def solution2(s):
    freq = [0]*26
    for i in s:
        freq[ord(i)-ord('a')] += 1
    for i in freq:
        if i == 0:
            return False
    return True

s = "Leetcode"
print(solution2(s))

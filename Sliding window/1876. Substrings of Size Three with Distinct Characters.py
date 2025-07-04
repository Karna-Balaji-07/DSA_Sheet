# 1876. Substrings of Size Three with Distinct Characters

def solutions1(s):
    arr = list(s)
    dicts = {}
    for i in range(len(arr)):
        dicts[i] = arr[i:i+3]
    count = 0
    for key,value in dicts.items():
        if len(set(value)) == 3:
            count += 1
    return count

def solutions2(s):
    count = 0
    for i in range(len(s)-2):
        substr = s[i:i+3]
        if len(set(substr)) == 3:
            count += 1
    return count
s = "xyzzaz"
print(solutions2(s))
# Check if all characters have equal number of occurrences

def solution1(s):
    dicts = {}
    for i in s:
        dicts[i] = dicts.get(i,0)+1
    s = list(set(dicts.values()))
    if len(s) ==1:
        return True
    return False


s = "aaabb"
print(solution1(s))
# Permutation difference between two strings

def solution1(s,t):
    dicts1 = {}
    dicts2 = {}
    for i in range(len(s)):
        dicts1[s[i]] = i

    for i in range(len(t)):
        dicts2[t[i]] = i
    sums = 0
    dicts1 = dict(sorted(dicts1.items()))
    dicts2 = dict(sorted(dicts2.items()))
    for key in dicts1.keys():
        sums += abs(dicts1[key] - dicts2[key])
    return sums


s = "abcde"; t = "edbac"
print(solution1(s,t))

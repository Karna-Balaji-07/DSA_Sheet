# 1461. Check If a String Contains All Binary Codes of Size K

def solutions1(s,k):
    total_combinations = 2**k
    dicts = {}
    for i in range(len(s)-k+1):
        binary = s[i:i+k]
        dicts[binary] = i
    return dicts

s = "0110"; k = 2
print(solutions1(s,k))
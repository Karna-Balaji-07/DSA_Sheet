# Find common characters

def solution1(arr):
    dicts = {}
    for i in arr[0]:
        dicts[i] = dicts.get(i,0)+1

    for i in arr[1:]:
        curr = {}
        for j in i:
            curr[j] = curr.get(j,0)+1

        for ch in list(dicts.keys()):
            if ch in curr:
                dicts[ch] = min(dicts[ch], curr[ch])
            else:
                dicts[ch] = 0

    result = []
    for key,value in dicts.items():
        result.extend([key]*value)
    return result

words = ["cool","lock","cook"]
print(solution1(words))
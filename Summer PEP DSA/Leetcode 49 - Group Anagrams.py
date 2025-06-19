# Group anagrams

def solution1(arr):
    result = []
    arrs = ["".join(sorted(word)) for word in arr]
    dicts = {}
    for i in range(len(arrs)):
        if arrs[i] not in dicts:
            dicts[arrs[i]] = len(result)
            result.append([])
        result[dicts[arrs[i]]].append(arr[i])

    return result

def hashfunction(s):
    freq = [0] * 26
    hashlist = []
    for i in s:
        freq[ord(i)-ord('a')] += 1
    for i in range(26):
        hashlist.append(str(freq[i]))
        hashlist.append('$')


    return "".join(hashlist)

def solution2(arr):
    result = []
    dicts = {}
    for i in range(len(arr)):
        hash = hashfunction(arr[i])
        if hash not in dicts:
            dicts[hash] = len(result)
            result.append([])
        result[dicts[hash]].append(arr[i])

    return result

arr = ["bdddddddddd","bbbbbbbbbbc"]
print(solution2(arr))
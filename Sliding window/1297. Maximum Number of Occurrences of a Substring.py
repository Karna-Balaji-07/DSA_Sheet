# 1297. Maximum Number of Occurrences of a Substring

def solutions1(arr,maxletters, minsize, maxsize):
    dicts = {}
    for i in range(len(arr)):
        if i+minsize <= len(arr) or i+maxsize <= len(arr):
            if len(set(arr[i:i + maxsize])) <= maxletters or len(set(arr[i:i + minsize])) <= maxletters :
                dicts[arr[i:maxsize+i]] = dicts.get(arr[i:maxsize+i],0)+1
                dicts[arr[i:minsize+i]] = dicts.get(arr[i:minsize+i],0)+1
    return dicts


def solutions2(arr,maxletters,minsize,maxsize):
    dicts = {}
    count = [0]*26
    maxocc = 0
    unique = 0
    left = 0
    right =0
    while right < len(arr):
        rightchar = arr[right]
        if count[ord(rightchar)-ord('a')] == 0:
            unique += 1
        count[ord(rightchar)-ord('a')] += 1

        right += 1
        if right - left > minsize:
            leftchar = s[left]
            if count[ord(leftchar)-ord('a')] == 1:
                unique -= 1
            count[ord(leftchar)-ord('a')] -= 1
            left += 1

        if right  - left == minsize and unique <= maxletters:
            subs = arr[left:right]
            dicts[subs] = dicts.get(subs,0)+1
            maxocc = max(maxocc,dicts[subs])

    return maxocc

s = "aababcaab"; maxLetters = 2; minSize = 3; maxSize = 4
print(solutions2(s,maxLetters,minSize, maxSize))

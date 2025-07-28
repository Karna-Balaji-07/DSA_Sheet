# 2559. Count Vowel Strings in Ranges

def solution(words, arr):
    n = len(words)
    vowels = ['a','e','i','o','u']
    prefix = [0]*len(words)
    for i in range(n):
        count += 1 if words[i][0] in vowels and words[i][1] in vowels else 0
        prefix[i+1] = prefix[i]+count
    result = []
    for left, right in arr:
        result.append(prefix[right+1]-prefix[left])
    return result
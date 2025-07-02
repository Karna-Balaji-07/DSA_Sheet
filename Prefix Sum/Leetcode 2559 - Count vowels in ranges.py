# count vowels in ranges

def solutions1(words, ranges):
    prefix = [0]* (len(words)+1)
    vowels = ['a','e','i','o','u']
    count = 0
    for i in range(len(words)):
        count = 1 if words[i-1][0] in vowels and words[i-1][-1] in vowels else 0
        prefix[i+1] = prefix[i] + count
    result = []
    for left, right in ranges:
        result.append(prefix[right+1]-prefix[left])
    return result
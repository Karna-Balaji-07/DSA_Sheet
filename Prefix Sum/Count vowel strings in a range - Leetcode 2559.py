# Count vowel strings in a range

def vowel(word):
    vowels = ['a','e','i','o','u']
    return word[0] in vowels and word[-1] in vowels

def solution(arr,ranges):

    prefix = [0] * (len(arr)+1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + (1 if vowel(arr[i]) else 0)
    result = []
    for left,right in ranges:
        result.append(prefix[right+1]- prefix[left])
    return result


words = ["aba","bcb","ece","aa","e"];queries = [[0,2],[1,4],[1,1]]
print(solution(words, queries))


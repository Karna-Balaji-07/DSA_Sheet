# sentence similarity III

def solution(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    len1 = len(words1)
    len2 = len(words2)
    if len1 < len2:
        words1,words2 = words2,words1
        len1,len2 = len2,len1
    start = 0
    end = 0
    while start < len2 and words1[start] == words2[start]:
        start  += 1
    while end < len2 and words1[len1-1-end] == words2[len2-1-end]:
        end += 1
    return start + end >= len2


sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(solution(sentence1,sentence2))
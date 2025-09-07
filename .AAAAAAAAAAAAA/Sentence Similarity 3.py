# Sentence Similarity

def solution(s1,s2):
    word1 = s1.split()
    word2 = s2.split()
    len1 = len(word1)
    len2 = len(word2)
    if len1 < len2:
        word1,word2 = word2,word1
        len1,len2 = len2,len1
    
    start = 0
    end = 0
    while start < len2 and word1[start] == word2[start]:
        start += 1
    while end < len2 and word1[len1-1-end] == word2[len2-1-end]:
        end +=1
    
    return start + end >= len2

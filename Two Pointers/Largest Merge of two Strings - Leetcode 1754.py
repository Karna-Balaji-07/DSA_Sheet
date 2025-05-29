def solution1(word1, word2):
    i = 0
    j = 0
    result = []
    while i < len(word1) and j < len(word2):
        if word1[i:] > word2[j:]:
            result.append(word1[i])
            i += 1
        else:
            result.append(word2[j])
            j += 1

    result.extend(word1[i:])
    result.extend(word2[j:])

    return result



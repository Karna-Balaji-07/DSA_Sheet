# 1160. Find Words That Can Be Formed by Characters

def solutions1(words, char):
    freq = [0]*26
    for i in char:
        freq[ord(i)-ord('a')] += 1
    result = 0
    for word in words:
        if canform(word, freq):
            result += len(word)
    return result


def canform(word, counts):
    charcount = [0]*26
    for i in word:
        x = ord(i)- ord('a')
        charcount[x] += 1
        if charcount[x] > counts[x]:
            return False
    return True



words = ["cat","bt","hat","tree"]; chars = "atach"
print(solutions1(words, chars))
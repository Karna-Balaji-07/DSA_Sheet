# Decode the message

def solution1(s,t):
    dicts = {}
    k = 97
    for i in s:
        if i not in dicts and i != ' ':
            dicts[i] = chr(k)
            k += 1

    result = ""
    for i in t:
        if i == ' ':
            result += " "
        else:
            result += dicts[i]
    return result



s = "the quick brown fox jumps over the lazy dog"
print(solution1(s,"vkbs bs t suepuv"))

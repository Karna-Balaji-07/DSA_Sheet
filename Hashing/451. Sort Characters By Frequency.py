# 451. Sort Characters By Frequency

def solutions1(s):
    dicts = {}
    for i in s:
        dicts[i] = dicts.get(i,0)+1

    result = ""
    sorted_dict = dict(sorted(dicts.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        result += (key)*value
    return result


s = "tree"
print(solutions1(s))
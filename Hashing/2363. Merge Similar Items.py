# 2363. Merge Similar Items

def solutions1(items1, items2):
    dicts = {}
    for value, weights in items1+items2:
        dicts[value] = dicts.get(value,0)+weights

    sorted_dict = dict((sorted(dicts.items(), key=lambda item: item[0])))
    result = []
    for key, value in sorted_dict.items():
        result.append([key,value])
    return result
items1 = [[1,1],[4,5],[3,8]]; items2 = [[3,1],[1,5]]
print(solutions1(items1,items2))

# sort elements by frequency

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1

    sorted_items = sorted(dicts.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for key,value in sorted_items:
        result.extend([key]*value)
    return result   


arr = [5, 5, 4, 6, 4]
print(solution1(arr))
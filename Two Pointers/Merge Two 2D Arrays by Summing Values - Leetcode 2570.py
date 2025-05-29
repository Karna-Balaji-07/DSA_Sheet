# Merge two 2d arrays by summing values

def merge(arr1, arr2):
    arr = arr1 + arr2
    dicts = {}
    for key, value in arr:
        if key in dicts:
            dicts[key] += value
        else:
            dicts[key] = value

    result = [[key, value] for key, value in sorted(dicts.items())]
    return result


arr1 = [[1, 2], [2, 3], [4, 5]]
arr2 = [[1, 4], [3, 2], [4, 1]]
print(merge(arr1, arr2))

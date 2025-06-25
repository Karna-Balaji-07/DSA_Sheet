# COntains DUplciate

def solution1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for values in dicts.values():
        if values > 1:
            return False
    return True

def solutions2(arr):
    s = set(arr)
    return len(s) == len(arr)

nums = [1,1,1,3,3,4,3,2,4,2]
print(solutions2(nums))
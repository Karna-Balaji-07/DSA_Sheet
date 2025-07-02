# 3158. Find the XOR of Numbers Which Appear Twice

def solutions1(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    result = 0
    for key,value in dicts.items():
        if value > 1:
            result ^= key

    return result

nums = [1,2,3,1]
print(solutions1(nums))
# sum of all unique elements

def solution1(arr):
    dicts = {}
    sums = 0
    for i in arr:
        dicts[i] = dicts.get(i,0)+1
    for key,values in dicts.items():
        if values == 1:
            sums += key
    return sums

nums = [1,1,1,1,1]
print(solution1(nums))
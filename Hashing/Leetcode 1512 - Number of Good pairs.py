# Number of good pairs

def solution(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1

    result = []
    for values in dicts.values():
        if values > 1:
            n= values
            count = n * (n-1) //2
            result.append(count)

    return sum(result)

nums = [1,2,3]
print(solution(nums))
# sort the jumbled numbers

def solution(mapping, arr):
    result = []
    arrs =[]
    for i in arr:
        l = ""
        s = str(i)
        for k in s:
            k = int(k)
            a = mapping[k]
            l += str(a)
        arrs.append(int(l))
    dicts = {}
    for i in range(len(arrs)):
        dicts[i] = arrs[i]

    sorted_by_values = dict(sorted(dicts.items(), key=lambda x: x[1]))
    for i in sorted_by_values.keys():
        result.append(arr[i])
    return result


mapping = [0,1,2,3,4,5,6,7,8,9]; nums = [789,456,123]
print(solution(mapping,nums))


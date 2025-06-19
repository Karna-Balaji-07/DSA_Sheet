# sort array by increasing frequency

def solution(arr):
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0)+1

    result = []
    sorted_items = sorted(dicts.items(), key=lambda x: (x[1], -x[0]))
    for key, value in sorted_items:
        result.extend([key]*value)

    return result

arr = [-1,1,-6,4,5,-6,1,4,1]
print(solution(arr))
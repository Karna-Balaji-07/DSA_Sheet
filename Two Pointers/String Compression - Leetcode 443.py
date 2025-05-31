# string compression

def solution(arr):
    result = []
    dicts = {}
    for i in arr:
        dicts[i] = dicts.get(i,0) +1
    for key,value in dicts.items():
        if value > 1:
            result.append(key)
            result.append(value)
        if value == 1:
            result.append(key)
    return len(result), result

def solution1(chars):
    left = 0
    n = len(chars)
    result = []
    while left < n:
        right = left + 1
        while right < n and chars[left] == chars[right]:
            right += 1
        count = right - left
        result.append(chars[left])
        if count != 1:
            for i in str(count):
                result.append(i)

        left = right
    chars[:] = result
    return len(chars)

arr = ["a","a","a","b","b","a","a"]
print(solution1(arr))
arr = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(solution1(arr))
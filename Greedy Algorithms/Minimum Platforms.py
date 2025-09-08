# Minimum Platforms

def solution(arr, dep):
    arr.sort()
    dep.sort()
    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans,count)
    return ans
# Intersection of two arrays

def solution1(arr1, arr2):
    first = len(arr1)
    last = len(arr2)
    result = []
    if first < last:
        for i in arr1:
            if i in arr2 and i not in result:
                result.append(i)
    else:
        for i in arr2:
            if i in arr1 and i not in result:
                result.append(i)

    return result

def solution2(arr1,arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    result = set()
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            result.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return list(result)

nums1 = [4,9,5]; nums2 = [9,4,9,8,4]
print(solution2(nums1,nums2))
# Merge Two 2d arrays by summing values

def solution1(nums1, nums2):
    dicts = {}
    arr = nums1+nums2
    for key, value in arr:
        if key in dicts:
            dicts[key] += value
        else:
            dicts[key] = value

    result = [[key,value] for key, value in sorted(dicts.items())]
    return result

def solution2(arr1,arr2):
    first = 0
    second = 0
    result = []
    while first < len(arr1) and second < len(arr2):
        if arr1[first][0] == arr2[second][0]:
            result.append([arr1[first][0], arr1[first][1]+arr2[second][1]])
            first += 1
            second += 1
        elif arr1[first][0] < arr2[second][0]:
            result.append(arr1[first])
            first += 1
        else:
            result.append(arr2[second])
            second += 1

    result.extend(arr1[first:])
    result.extend(arr2[second:])
    return result
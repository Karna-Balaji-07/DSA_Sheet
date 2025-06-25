# Find common elements between arrays

def solution1(arr1, arr2):
    count1 = 0
    count2 = 0
    for i in arr1:
        if i in arr2:
            count1 += 1

    for i in arr2:
        if i in arr1:
            count2 += 1
    return [count1, count2]

def solution2(arr1, arr2):
    arrs1 = set(arr1)
    arrs2 = set(arr2)
    common = arrs1.intersection(arrs2)
    count1 = 0
    for i in arr1:
        if i in common:
            count1 += 1
    count2 = 0
    for i in arr2:
        if i in common:
            count2 += 1
    return [count1, count2]

nums1 = [4,3,2,3,1]; nums2 = [2,2,5,2,3,6]
print(solution2(nums1,nums2))
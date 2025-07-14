# 496. Next Greater Element I

def solutions1(arr1,arr2):
    arr = []
    stack = []
    for i in range(len(arr2)-1,-1,-1):
        while stack and stack[-1]<arr2[i]:
            stack.pop()
        if stack and arr2[i] < stack[-1]:
            arr.append([arr2[i],stack[-1]])
        stack.append(arr2[i])

    dicts = {first:second for first, second in arr}
    result = [dicts[x] if x in dicts else -1 for x in arr1]
    return result

nums1 = [2,4]; nums2 = [1,2,3,4]
print(solutions1(nums1,nums2))
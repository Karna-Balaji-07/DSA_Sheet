# 2605. Form Smallest Number From Two Digit Arrays

def solutions1(arr1, arr2):
    intersection = list(set(arr1) & set(arr2))
    if intersection:
        intersection.sort()
        return str(intersection[0])
    else:
        num1 = min(arr1)
        num2 = min(arr2)
        result = int(str(min(num1, num2)) + str(max(num1, num2)))
        return result

nums1 = [4,1,3]; nums2 = [5,7]
print(solutions1(nums1, nums2))
nums1 = [3,5,2,6]; nums2 = [3,1,7]
print(solutions1(nums1, nums2))

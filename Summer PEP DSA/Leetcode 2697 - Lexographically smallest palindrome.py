# lexicographically smallest palindrome

def solution1(s):
    n = len(s)
    arr = []
    for i in s:
        arr.append(i)

    left = 0
    right = n-1
    while left < right:
        if arr[left] != arr[right]:
            if arr[left] < arr[right]:
                arr[right] = arr[left]
            else:
                arr[left] = arr[right]
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1
    return "".join(arr)

s = "egcfe"
print(solution1(s))
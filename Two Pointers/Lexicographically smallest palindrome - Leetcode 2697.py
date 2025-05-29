# Lexicographically smallest palindrome

def palindrome(s):
    arr = []
    for i in s:
        arr.append(i)

    n = len(arr)
    left = 0
    count = 0
    right = n-1
    while left < right:
        if arr[left] != arr[right]:
            arr[right] = arr[left]
            left += 1
            right -= 1
            count += 1
        else:
            left += 1
            right -= 1

    return arr, count


s = "seven"
print(palindrome(s))
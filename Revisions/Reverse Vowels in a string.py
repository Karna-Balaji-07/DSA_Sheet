# Reverse vowels in a string

def solution(arr):
    arr = list(arr)
    vowels = "aeiouAEIOU"
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] in vowels and arr[right] in vowels:
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -= 1
        elif arr[left]  not in vowels:
            left +=1
        elif arr[right] not in vowels:
            right -=1
        
    return "".join(arr)

s = "IcErEAm"
print(solution(s))
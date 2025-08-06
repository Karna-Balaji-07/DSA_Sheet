# Reverse words in a string

def solution(arr):
    arr = arr.split()
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return " ".join(arr)

arr = "Sky is Blue"
print(solution(arr))
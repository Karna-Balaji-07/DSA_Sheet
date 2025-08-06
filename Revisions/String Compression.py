# String compression

def solution(arr):
    left  = 0
    n = len(arr)
    result = []
    while left < n:
        right = left +1
        while right < n and arr[right] == arr[left]:
            right +=1
        count = right-left
        result.append(arr[left])
        if count != 1:
            for i in str(count):
                result.append(i)
        
        left = right
    return result

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(solution(chars))
# 15. 3Sum : sum == 0

def solution(arr):
    arr.sort()
    result = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left < right:
            curr = arr[i] + arr[left] + arr[right]
            if curr < 0:
                left += 1
            elif curr > 0:
                right -= 1
            
            else:
                result.append([arr[i],arr[left],arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left +=1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left +=1
                right -= 1
            
    return result
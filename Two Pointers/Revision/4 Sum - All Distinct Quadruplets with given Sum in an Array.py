# 4 Sum - All Distinct Quadruplets with given Sum in an Array

def solution(arr, target):
    result = []
    n = len(arr)
    arr.sort()
    for first in range(n-3):
        if first >= 0 and arr[first] == arr[first-1]:
            continue
        for second in range(1+first,n-2):
            if second > first+1 and arr[second] == arr[second-1]:
                continue    
            third = second+1
            fourth = n-1
            while third < fourth:
                sums = arr[first]+arr[second]+arr[third] + arr[fourth]
                if sums == target:
                    result.append([arr[first], arr[second],arr[third],arr[fourth]])
                    third +=1
                    fourth -=1
                    while third < fourth  and arr[third] ==arr[third-1]:
                        third +=1
                    while third < fourth and arr[fourth] == arr[fourth+1]:
                        fourth -=1
                elif target > sums:
                    third +=1
                else:
                    fourth -=1
    return result

arr = [10, 2, 3, 4, 5, 7, 8]
target = 23
print(solution(arr,target))                        
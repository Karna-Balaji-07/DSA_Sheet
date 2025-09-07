# 4sum

def solution(arr,target):
    result = []
    arr.sort()
    n = len(arr)
    for first in range(n-3):
        if first > 0 and arr[first] == arr[first-1]:
            continue
        for second in range(n-2):
            if second > first and arr[second] == arr[second-1]:
                continue
            third = second+1
            fourth = n-1
            while third < fourth:
                sums = arr[first] + arr[second] + arr[third] + arr[fourth]
                if sum > target:
                    fourth -=1
                elif sums < target:
                    third +=1
                else:
                    result.append([first,second,third,fourth])
                    while third < fourth and arr[third] == arr[third+1]:
                        third +=1
                    while third < fourth and arr[fourth] == arr[fourth-1]:
                        fourth -=1
                    third +=1
                    fourth -=1
    return result
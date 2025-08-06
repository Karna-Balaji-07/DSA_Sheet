# 3Sum problem

def solution1(arr,target):
    result = []
    n = len(arr)
    for first in range(n-2):
        if first > 0 and arr[first] == arr[first-1]:
            continue
        second = first+1
        third = n -1 
        while second < third:
            sums = arr[first] + arr[second] + arr[third]
            if sums > 0:
                third -=1
            elif sums< 0:
                second +=1
            else:
                result.append([first,second,third])
                while second <  third and arr[second] == arr[second+1]:
                    second +=1
                while second  < third and arr[third] == arr[third-1]:
                    third -= 1
                second +=1
                third -=1
    return result
# 4 Sum - Check if a Quadruple with given Sum Exists in an Array

def solution(arr, target):
    result = 0
    arr.sort()
    n = len(arr)
    for first in range(n-3):
        for second in range(n-2):
            third = second+1
            fourth = n-1
            while fourth > third:
                result = arr[first]+arr[second]+arr[third]+arr[fourth]
                if result > target:
                    fourth -=1
                elif result < target:
                    third +=1
                else:
                    return True
            
    return False 

def solution1(arr, target):
    dicts = {}
    n = len(arr)
    count = 0
    seen = set()
    for i in range(n-1):
        for j in range(1+i,n):
            sums = arr[i]+arr[j]
            if sums not in dicts:
                dicts[sums] = []
            dicts[sums].append((i,j))
            
        
    for i in range(n-1):
        for j in range(i+1,n):
            sums = arr[i]+arr[j]
            diff = target - sums
            if diff in dicts:
                for p in dicts[diff]:
                
                    if p[0] != i and p[0] != j and p[1] != i and p[1] != j:
                        quad = tuple(sorted([arr[i], arr[j], arr[p[0]], arr[p[1]]]))
                        if quad not in seen:
                            seen.add(quad)
                            count +=1
    return count

arr = [1, 5, 3, 1, 2 ,10]
target = 20
print(solution1(arr, target)) 
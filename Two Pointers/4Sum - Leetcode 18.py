# 4 sum problem

def solution1(arr, target):
    result = set()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            s = set()
            for k in range(j+1,n):
                sums = arr[i] + arr[j] + arr[k]
                last = target - sums
                if last in s:
                    curr = sorted([arr[i],arr[j],arr[k],last])
                    result.add(tuple(curr))
                s.add(arr[k])

    arrs = list(result)
    return arrs

def solution2(arr,target):
    result = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target:
                    result.append([arr[i],arr[j],arr[k],arr[l]])
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                     l -= 1

    return result

arr = [10, 2, 3, 4, 5, 7, 8]
target = 23
print(solution2(arr,target))

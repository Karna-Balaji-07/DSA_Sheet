# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

def solutions1(arr,k, threshold):
    n = len(arr)
    count = 0
    for i in range(n-k+1):
        sums = sum(arr[i:i+k])
        avg = sums//k
        if avg >= threshold:
            count += 1

    return count

def solutions2(arr,k,threshold):
    n = len(arr)
    count = 0
    sums = 0
    for i in range(n):
        sums += arr[i]
        if i >= k:
            sums -= arr[i-k]
        if i >= k-1:
            avg =  sums//k
            if avg >= threshold:
                count += 1

    return count



arr = [2,2,2,2,5,5,5,8]; k = 3; threshold = 4
print(solutions2(arr,k,threshold))
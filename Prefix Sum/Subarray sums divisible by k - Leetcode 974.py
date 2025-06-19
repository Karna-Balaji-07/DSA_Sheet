# subarray sum divisible by k

def solution(arr,k):
    n = len(arr)
    dicts = {0:1}
    sums = 0
    count =0
    for i in range(n):
        sums += arr[i]
        remainder = sums % k
        if remainder < 0:
            remainder += k

        count += dicts.get(remainder,0)
        dicts[remainder] = dicts.get(remainder,0)+1
    return count

arr =  [4,5,0,-2,-3,1];k = 5
print(solution(arr,k))
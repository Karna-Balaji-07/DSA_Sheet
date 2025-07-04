# subarray sum divisible by k

def solutions1(arr,k):
    dicts= {}
    sums = 0
    result = 0
    for i in range(len(arr)):
        sums += arr[i]
        rem = sums % k
        if rem == 0:
            result += 1
        if rem < 0:
            rem += k

        result += dicts.get(rem,0)
        dicts[rem] = dicts.get(rem,0)+1
    return result

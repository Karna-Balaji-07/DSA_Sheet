# subarray sum equals k

def solutoin1(arr,k):
    curr_sum = 0
    dicts = {}
    ans = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == k:
           ans += 1
        if curr_sum - k in dicts:
            ans += dicts[curr_sum-k]
        dicts[curr_sum] = dicts.get(curr_sum,0)+1
    return ans


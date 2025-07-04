# Make sum divisible by k


def solution1(arr,k):
    total = sum(arr)
    rem = total % k
    if rem == 0:
        return 0

    dicts = {0:-1}
    curr_sum = 0
    min_length = len(arr)

    for i in range(len(arr)):
        curr_sum += arr[i]
        curr_rem = curr_sum % k
        target = (curr_rem - rem + k) % k
        if target in dicts:
            min_length = min(min_length, i-dicts[target])

        dicts[curr_rem] = i

    return -1 if min_length == len(arr) else min_length

arr = [3,1,4,2]
k = 6
print(solution1(arr,k))
nums = [6,3,5,2]; p = 9
print(solution1(nums,p))


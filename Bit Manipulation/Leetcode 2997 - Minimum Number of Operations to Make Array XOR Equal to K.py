# Minimum Number of Operations to Make Array XOR Equal to K

def solution1(arr,k):
    res = 0
    for i in arr:
        res ^= i

    return bin(res - k).count('1')

nums = [2,0,2,0];k = 0
print(solution1(nums,k))
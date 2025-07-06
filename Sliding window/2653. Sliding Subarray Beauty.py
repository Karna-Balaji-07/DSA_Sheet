# 2653. Sliding Subarray Beauty

def solutions1(nums,k,x):
    freq = [0] * 51
    result = []
    temp = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            freq[abs(nums[i])] += 1
        if i - temp + 1 >= k:
            count = 0
            for l in reversed(range(51)):
                count += freq[l]
                if count >= x:
                    result.append(-l)
                    break

            if count < x:
                result.append(0)
            if nums[temp] < 0:
                freq[abs(nums[temp])] -= 1
            temp += 1
    return result


arr = [1,-1,-3,-2,3]
k = 3
x = 2
print(solutions1(arr,k,x))
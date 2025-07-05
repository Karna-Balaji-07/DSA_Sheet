# 2090. K Radius Subarray Averages

def solutions1(arr,k):
    diameter =  2*k+1
    sums = 0
    arrs = [-1]*len(arr)
    for i in range(len(arr)):
        sums += arr[i]

        if i >= diameter-1:
            avg = sums // diameter
            arrs[i-k] = avg
            sums -= arr[i - diameter + 1]
    return arrs


nums = [7,4,3,9,1,8,5,2,6]; k = 3
print(solutions1(nums,k))
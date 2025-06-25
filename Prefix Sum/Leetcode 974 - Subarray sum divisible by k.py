def subarraysDivByK(nums, k: int) -> int:
    len(nums)
    dicts  = {0:1}
    sums = 0
    count = 0
    for i in nums:
        sums += i
        remainder = sums % k
        if remainder < 0:
            remainder += k
        count += dicts.get(remainder,0)
        dicts[remainder] = dicts.get(remainder,0)+1
    return count


class Solution:
    pass

obj = Solution()
print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
print(-4//5)

def nonNegativeAverage(arr):
    total = 0
    #Write your code to find average of positive numbers in number list
    #Return the answer
    count = 0
    for x in arr:
        if x>=0:
            total += x
            count += 1
    avg = total // count
    return avg

arr = [1,2,4,-1,-2,-5,-6]
print(nonNegativeAverage(arr))
    
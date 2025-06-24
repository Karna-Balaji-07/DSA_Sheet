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


    
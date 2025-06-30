# single number 2

def solution1(arr):
    ans = 0
    base = 1
    for i in range(32):
        count0 = 0
        count1 = 0
        for num in arr:
            if num & (1 << i) > 0:
                count1 += 1
            else:
                count0 += 1

        if count1 % 3 != 0:
            ans = ans * base + 1
            base *= 10
        else:
            ans *= base + 0
            base *= 10
    return ans

arr = [2,2,3,2]
print(solution1(arr))
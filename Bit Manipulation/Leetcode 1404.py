#  Number of Steps to Reduce a Number in Binary Representation to One

def solution1(s):
    n = len(s)
    num = 0
    for i in range(n):
        bit = int(s[n - 1 - i])  # from right to left
        num += bit * (2 ** i)

    count = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            count += 1
        else:
            num += 1
            count += 1
    return count

            

s = "1101"
print(solution1(s))
# Happy Number

def solution1(n):
    num = n
    sumss = 0
    while sumss != 1 and sumss > 9:
        sumss = 0
        while num:
            digit = num % 10
            sumss += digit ** 2
            num = num // 10
        num = sumss
    if sumss == 1:
        return True
    return False

n = 9
print(solution1(n))


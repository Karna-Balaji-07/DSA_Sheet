# Minimum bit flips to convert number

def solution1(start, end):
    res = bin(start  ^ end)
    return res.count('1')

def solution2(start,end):
    count = 0
    while start > 0 or end > 0:
        curr1  = start & 1
        curr2 = end & 1
        if curr1 != curr2:
            count += 1
        start >>= 1
        end >>= 1
    return count

start = 10
end = 7
print(solution2(start,end))
# Conting bits

def solution(n):
    result = [0]
    for i in range(1,n+1):
        count = 0
        while i > 0:
            rem =i % 2
            if rem == 1:
                count += 1
            i = i // 2
        result.append(count)
    return result

def solution2(n):
    result = [0]*(n+1)
    for i in range(1, n+1):
        if i % 2 == 0:
            result[i] = result[i//2]
        else:
            result[i] = result[i//2]+1
    return result

n = 5
print(solution2(n))


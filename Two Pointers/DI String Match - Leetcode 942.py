# DI string match

def solution1(s):
    low = 0
    n = len(s)
    high = n
    result = []
    for i in s:
        if i == 'I':
            result.append(low)
            low +=1
        else:
            result.append(high)
            high -= 1

    result.append(low)
    return result


s = "IDID"
print(solution1(s))
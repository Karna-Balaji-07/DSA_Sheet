# Largest number

def solution1(arr):
    strings = [str(i) for i in arr]
    n = len(strings)
    for i in range(n):
        for j in range(i+1,n):
            if strings[j] + strings[i] > strings[j] + strings[i]:
                strings[i],strings[j] = strings[j],strings[i]

    if arr[0] == '0':
        return '0'

    return ''.join(strings)

arr = [3,30,34,5,9]
print(solution1(arr))
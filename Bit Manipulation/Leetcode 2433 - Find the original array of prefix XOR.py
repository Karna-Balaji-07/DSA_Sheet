# Find the original array of prefix XOR

def solution1(arr):
    result = []
    prev = 0
    for i in arr:
        result.append(prev ^ i)
        prev = i
    return result

pref = [5,2,0,3,1]
print(solution1(pref))
# sort string of characters

def solution1(arr):
    return "".join(sorted(arr))

def solution2(arr):
    count = [0] * 26
    for i in arr:
        count[ord(i)-ord('a')] += 1

    for i, counts in enumerate(count):
        if counts > 0:
            print((chr(i+ord('a')))*counts,end="")

arr = "geeksforgeeks"
print(solution2(arr))
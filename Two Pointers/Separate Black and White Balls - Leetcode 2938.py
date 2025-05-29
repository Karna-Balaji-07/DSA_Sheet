# Separate Black and White Balls

def solution1(s):
    arr= []
    for i in s:
        arr.append(i)

    i = 0
    count = 0
    swapped = True
    n = len(arr)
    while swapped:
        swapped = False
        i = 0
        while i < n-1:
            if arr[i] == "1" and arr[i+1] == "0":
                arr[i],arr[i+1] = arr[i+1],arr[i]
                count += 1
                swapped  = True
                i += 1

            i += 1

    return count


s = "100"
print(solution1(s))



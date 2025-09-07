# Jump Game

def solution(arr):
    maxindex= 0
    for i in range(len(arr) ):
        if i > maxindex:
            return False
        maxi = i + arr[i]
        maxindex = max(maxi, maxindex)

    return True

        
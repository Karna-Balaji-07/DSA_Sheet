# Seperate black and white balls

def solution(s):
    n = len(s)
    swap = 0
    black = 0
    for i in s:
        if i == '0':
            swap += black
        else:
            black += 1
    return swap


s = "10100"
print(solution(s))
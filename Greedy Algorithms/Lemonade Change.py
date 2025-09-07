# Lemonade Change

def solution(arr):
    five = 0
    ten = 0
    for i in range(len(arr)):
        if arr[i] == 5:
            five += 1
        elif arr[i] == 10:
            if five:
                five -= 1
                ten += 1
            else:
                return False
            
        else:
            if five and ten:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
            
    return True
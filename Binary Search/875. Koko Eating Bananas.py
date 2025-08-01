# 875. Koko Eating Bananas

def timecalc(hour,pile,mid):
    hours = 0
    for i in range(len(pile)):
        hours += pile[i] // mid
        if pile[i] % mid != 0:
            hours +=1
        
    return hours <= hour 
    

def solution(piles, hours):
    high = max(piles)
    low = 1
    result = max(piles)
    while  low <= high:
        mid = (low+high)//2
        if timecalc(hours, piles, mid) == True:
            result = mid
            high = mid-1
        else:
            low = mid+1
            
    return result
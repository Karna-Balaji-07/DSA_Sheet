from collections import defaultdict
def solution(n,reserved):
    reserved_rows = defaultdict()
    for row,seat in reserved:
        reserved_rows[row].add(seat)
    
    groups = 0
    for row in reserved_rows:
        reserveds = reserved_rows[row]
        left = all(seat not in reserveds for seat in [2,3,4,5])
        middle = all(seat not in reserveds for seat in [6,7,4,5])
        right = all(seat not in reserveds for seat in [6,7,8,9])
        if left and right:
            groups += 2
        elif left or right or middle:
            groups += 1
        
        
        
    unaffected = n - len(reserved_rows)
    groups += 2*unaffected
    return groups


        
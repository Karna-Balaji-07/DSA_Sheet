# Fractional Knapsack

def solution(values, weights,capacity):
    items = []
    for value, weight in zip(values, weights):
        items.append((value, weight, value/weight))
        
    items.sort(key = lambda x : x[2],reverse=True)
    total = 0.0
    remaining = capacity
    for value, weight, ratio in items:
        if remaining >= weight:
            total += value
            remaining -= weight
            
        else:
            total += value * (remaining/weight)
            break
        
    return round(total,6)


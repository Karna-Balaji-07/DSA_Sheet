# 2448. Minimum Cost to Make Array Equal

def solution(arr, cost):
    combined = sorted(zip(arr, cost))
    n = len(combined)
    prefix_multiplied_costs = [0]* (n+1)
    prefix_costs = [0]*(n+1)
    
    for i in range(1,n+1):
        num,cost = combined[i-1]
        prefix_multiplied_costs[i] = prefix_multiplied_costs[i-1] + num * cost
        prefix_costs[i] = prefix_costs[i-1]+cost
        
    result = float('inf')
    for i in range(1,n+1):
        pivot = combined[i-1][0]
        left = pivot * prefix_costs[i-1]-prefix_multiplied_costs[i-1]
        right = prefix_multiplied_costs[n] - prefix_multiplied_costs[i]-pivot * (prefix_costs[n] - prefix_costs[i])
        result = min(result, left+right)
    
    return result

def solution2(arr,cost):
    combined = sorted(zip(arr,cost))
    total = sum(cost)
    acc = 0
    median = 0
    for i,c in combined:
        acc += c
        if acc  >= (total+1)//2:
            median = i
            break
    
    result = 0
    for num,cost in combined:
        result += abs(num-median)*cost
    return result
        
                
nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518]
cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
print(solution2(nums,cost))

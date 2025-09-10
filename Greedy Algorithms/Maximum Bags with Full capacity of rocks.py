# Maximum bags with full capacity of rocks

def solution(capacity, rocks, additional):
    difference = [0]*len(rocks)
    for i in range(len(rocks)):
        difference[i] = capacity[i] - rocks[i]
    count = 0
    difference.sort()
    for i in range(len(rocks)):
        if difference[i] > additional:
            break
        additional -= difference[i]
        count += 1
    return count

capacity = [2,3,4,5]; rocks = [1,2,4,4]; additionalRocks = 2
print(solution(capacity, rocks,additionalRocks))
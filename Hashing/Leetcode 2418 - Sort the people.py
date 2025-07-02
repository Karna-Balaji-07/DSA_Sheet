# sort the people

def solutions1(people, heights):
    dicts = {}
    for i in range(len(heights)):
        dicts[heights[i]] = i
    sorted_heights = dict(sorted(dicts.items()))
    result = []
    for key, value in sorted_heights.items():
        result.append(people[value])
    return result[::-1]

names = ["Mary","John","Emma"];heights = [180,165,170]
print(solutions1(names,heights))
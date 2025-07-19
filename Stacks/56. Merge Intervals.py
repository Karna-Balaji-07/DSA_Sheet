# 56. Merge Intervals

def solution(arr):
    arr.sort()
    result = [arr[0]]
    if len(arr) == 1:
        return arr
    for i in range(1,len(arr)):
        current = result[-1]
        if current[1] > arr[i][0]:
            current[1] = max(current[1], arr[i][1])
        else:
            result.append(arr[i])
    return result

def solution(arr):
    if not arr:
        return []

    arr.sort()  # Sort by starting time
    result = [arr[0]]  # Initialize with the first interval

    for i in range(1, len(arr)):
        last = result[-1]
        current = arr[i]

        # Check for overlap
        if current[0] <= last[1]:
            # Merge intervals
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add the current interval
            result.append(current)

    return result

# Example usage
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution(intervals))

intervals = [[1,4],[5,7]]
print(solution(intervals))
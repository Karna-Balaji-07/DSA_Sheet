def preprocess(s):
    n = len(s)
    
    # Prefix sum of plates ('*')
    plates_prefix = [0] * (n + 1)
    
    # Nearest candle to the left of or at i
    left = [-1] * n
    # Nearest candle to the right of or at i
    right = [-1] * n
    
    for i in range(n):
        plates_prefix[i+1] = plates_prefix[i] + (1 if s[i] == '*' else 0)
    
    last = -1
    for i in range(n):
        if s[i] == '|':
            last = i
        left[i] = last
    
    last = -1
    for i in range(n-1, -1, -1):
        if s[i] == '|':
            last = i
        right[i] = last
    
    return left, right, plates_prefix

def solution(s, queries):
    lefts, rights, plates_prefix = preprocess(s)
    result = []
    for start, end in queries:
        left_candle = rights[start]
        right_candle = lefts[end]
        if left_candle != -1 and right_candle != -1 and left_candle < right_candle:
            plates = plates_prefix[right_candle] - plates_prefix[left_candle]
            result.append(plates)
        else:
            result.append(0)
    return result

# Test
s = "***|**|*****|**||**|*"
queries = [[1,17], [4,5], [14,17], [5,11], [15,16]]
print(solution(s, queries))  # Output: [9, 0, 0, 0, 0]

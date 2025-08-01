# Distinct Numbers

def solution(arr):
    return len(set(arr))

n = int(input())
arr = list(map(int,input().split()))
result = solution(arr)
print(result)
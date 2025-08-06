# Range sum query

def solution(arr,queries):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    print(prefix)
    for query in queries:
        i,j = query
        if i == 0:
            sums = prefix[j]
        else:
            sums = prefix[j] - prefix[i-1]
        print(sums)
arr = [-2, 0, 3, -5, 2, -1]
queries = [[0, 2], [2, 5], [0, 5]]
solution(arr,queries)  
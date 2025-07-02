# Array manipulation

def solutions1(n, queries):
    prefix = [0]* (n+1)
    for query in queries:
        a,b,k = query
        prefix[a-1] += k
        if b < n:
            prefix[b] -= k

    naxvalue = 0
    current_sum = 0
    for val in prefix:
        current_sum += val
        naxvalue = max(current_sum, naxvalue)

    return naxvalue


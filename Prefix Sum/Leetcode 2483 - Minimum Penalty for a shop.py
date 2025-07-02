# minimum penalty for a shop

def solutions1(s):
    n = len(s)
    prefix = [0] * (n+1)
    suffix = [0] * (n+1)
    for i in range(1,n+1):  # when shop is open and no customers come
        if s[i] == 'N':
            prefix[i] = prefix[i-1] +1
        else:
            prefix[i] = prefix[i-1]

    for i in range(n-1,-1,-1): # when shop is close and customers comes
        if s[i] == 'Y':
            suffix[i] = suffix[i+1] +1
        else:
            suffix[i] = suffix[i+1]

    honouring = 0
    penalty = float('inf')
    for i in range(n+1):
        curr = prefix[i] + suffix[i]
        if curr < penalty:
            penalty = curr
            honouring = i

    return honouring


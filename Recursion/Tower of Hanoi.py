# Hanoi tower

def solution(n,fromm, to, aux):
    if n == 0:
        return
    solution(n-1,fromm, aux, to)
    print(f'{fromm} {to}')
    solution(n-1,aux, to, fromm)
    
    

def solutions(n,fromm, to, aux):
    if n == 0:
        return 0
    counts = 0
    counts += solutions(n-1,fromm, aux, to)
    counts  += 1
    counts += solutions(n-1,aux, to, fromm)
    return counts
n = 3
solution(n,'A','C','B')
print(solutions(n,'A','C','B'))
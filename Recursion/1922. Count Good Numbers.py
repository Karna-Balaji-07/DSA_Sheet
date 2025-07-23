# 1922. Count Good Numbers

def solution(n):
    mod = 10**9+7
    def pow(base,exponent):
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (base*result) % mod
            base= (base*base) % mod
            exponent //= 2
        return result
    
    return (pow(5,(n+1)//2) * pow(4,n//2)) % mod

n  = 4
print(solution(n))
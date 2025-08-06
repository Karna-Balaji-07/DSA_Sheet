# Valid Palindrome

def solution(arr):
    arr = list(arr)
    s = "".join(s.lower() for s in arr if s.isalpha())
    return s==s[::-1]
    

s = "A man, a plan, a canal: Panama"
print(solution(s))
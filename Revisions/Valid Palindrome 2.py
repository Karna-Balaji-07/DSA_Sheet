# valid palindrome II

def valid(left, right,arr):
    while left < right:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -=1
    return True
def solution(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return valid(left,right-1,s) or valid(left+1,right,s)
        left +=1
        right -=1
    return True

s = "abcd"
print(solution(s))
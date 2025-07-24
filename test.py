# cook your dish here
n = int(input())
x,y = map(int,input().split())
arr = list(map(int,input().split()))

def solution(n,x,y,arr):
    while y > 0:
        arr.sort()
        s= (arr[0] + arr[1])
        if s % 2 == 0:
            avg = s//2
        else:
            avg =(s+1)//2 
        y -= 1
    arr.append(avg)
    sums = sum(arr)
    print(sums)
solution(n,x,y,arr)
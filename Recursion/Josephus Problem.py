# Josephus problem

def solution(arr,k,index =0):
    if len(arr) == 1:
        print(arr[0])
        return
    
    index = (index+k-1) % len(arr)
    del arr[index]
    solution(arr,k,index)
    
    

n = 5
arr = [i for i in range(1,n+1)]
k = 3
solution(arr,k)
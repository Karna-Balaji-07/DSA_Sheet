class Solution:
    def josephus(self,n,k):
        #code here
        arr = [i for i in range(1,n+1)]
        def safe(arr,k,index=0):
            if len(arr)==1:
                return arr[0]
            
            index = (index+k-1) % len(arr)
            del arr[index]
            return safe(arr,k,index)
        return safe(arr,k)
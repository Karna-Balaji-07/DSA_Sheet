# Delete middle element of the stack without using extra data structure

def solution(stack):
    mid = len(stack)//2
    def midle(stack,stacksize,current):
        if current ==  stacksize//2:
            stack.pop()
            return
    
        x = stack.pop()
        current +=1
        midle(stack,stacksize,current)
        stack.append(x)
        
    midle(stack,len(stack),0)
    return stack
stack = [10,20,30,40,50]
print(solution(stack))
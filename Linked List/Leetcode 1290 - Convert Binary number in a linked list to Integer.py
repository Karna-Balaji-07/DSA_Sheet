# convert binary number in linked list to integer

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next

    sums = 0
    arr = arr[::-1]
    for i in range(len(arr)):
        if arr[i]  != 0:
            sums += 2**i
    return sums

def solution2(head):
    temp = head
    curr = head
    count = 0
    while temp:
        count += 1
        temp = temp.next

    count -= 1
    sums = 0
    while curr:
        if curr.data == 1:
            sums += pow(2,count)
        count -= 1
        curr = curr.next
    return sums

head = Node(1)
head.next = Node(0)
head.next.next = Node(1)

result = solution2(head)
print(result)
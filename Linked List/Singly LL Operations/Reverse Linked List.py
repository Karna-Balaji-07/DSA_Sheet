# reverse the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode

    return prev

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(6)
head.next.next.next.next = Node(5)
printLL(head)
print()
result = reverse(head)
printLL(result)
# Print the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next

head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
printLL(head)
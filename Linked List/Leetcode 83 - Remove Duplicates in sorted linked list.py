# remove duplicates in sorted linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    temp = head
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next


    curr = head
    while curr:
        print(curr.data,end=" ")
        curr = curr.next


head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(4)

solution1(head)
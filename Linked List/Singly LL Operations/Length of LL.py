# Length of the Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def length(head):
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next

    return count

def rec_length(head):
    if head is None:
        return 0
    return 1  + rec_length(head.next)


head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print(length(head))
print(rec_length(head))
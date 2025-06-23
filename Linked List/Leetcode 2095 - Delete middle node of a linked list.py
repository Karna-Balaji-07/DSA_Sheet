# Delete the middle node  of a linked list
from encodings.hex_codec import hex_decode


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def solution1(head):
    curr = head
    count = 0
    while curr:
        count += 1
        curr =curr.next

    curr = head
    middle = count // 2
    for i in range(middle -1):
        curr = curr.next
    curr.next = curr.next.next
    return head

def solution2(head):
    slow = head
    fast = head
    if head.next is None:
        return None
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    return head

def printll(head):
    while head:
        print(head.data, end=" ")
        head = head.next



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = solution2(head)
printll(result)


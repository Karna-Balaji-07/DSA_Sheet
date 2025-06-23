# sort linked list

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def solution1(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.data)
        curr = curr.next

    arr.sort()
    dummy = Node(-1)
    curr = dummy
    for i in arr:
        curr.next = Node(i)
        curr = curr.next
    return dummy.next


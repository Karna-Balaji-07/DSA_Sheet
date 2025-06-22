# Insert a node at a specific position in the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(pos,head,data):
    if pos < 1:
        return head
    if pos == 1:
        node = Node(data)
        node.next = head
        return node

    curr = head
    for _ in range(1,pos-1):
        if curr is None:
            break
        curr = curr.next

    if curr is None:
        return head

    node = Node(data)
    node.next = curr.next
    curr.next = node

    return head
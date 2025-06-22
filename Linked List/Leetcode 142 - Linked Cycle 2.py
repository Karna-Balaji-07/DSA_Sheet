# Linked list cycle II

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.data

head = Node(1)
head.next = Node(3)
head.next.next = Node(4)

# Create a loop
head.next.next.next = head.next

print(solution1(head))
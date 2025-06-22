# cycle in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    slow = head
    fast = head
    while slow and  fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


head = Node(1)
head.next = Node(3)
head.next.next = Node(4)

# Create a loop
head.next.next.next = head.next

print(solution1(head))
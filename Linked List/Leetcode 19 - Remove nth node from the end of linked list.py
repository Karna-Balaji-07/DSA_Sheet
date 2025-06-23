# Remove nth node from the end of the linked list

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def solution1(head, target):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    if count - target == 0:
        return head.next

    curr = head
    for _ in range(1,count-target):
        curr = curr.next

    curr.next = curr.next.next
    return head

def solution2(head,n):
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head = solution2(head,4)
curr = head
while curr:
    print(curr.data, end=" ")
    curr = curr.next
print()
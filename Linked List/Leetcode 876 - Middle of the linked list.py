# Middle of the linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    temp = head
    count =0
    while temp:
        count += 1
        temp = temp.next

    count //= 2
    curr = head
    for _ in range(count):
        curr = curr.next
    return curr

def solution2(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
result = solution2(head)
print(result.data)
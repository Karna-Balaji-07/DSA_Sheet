# Palindrome linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next

    return arr == arr[::-1]

def reverse(head):
    curr = head
    prev = None
    while curr:
        newnode = curr.next
        curr.next = prev
        prev  =curr
        curr = newnode
    return prev

def solution2(head):
    if not head and not head.next:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = reverse(slow)
    first = head
    temp = second
    while temp:
        if temp.data != first.data:
            return False
        temp = temp.next
        first = first.next

    return True

head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print(solution2(head))
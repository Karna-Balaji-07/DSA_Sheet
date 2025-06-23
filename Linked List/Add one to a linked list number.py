# add 1 to a linked list number

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def solution1(head):
    s = ""
    temp = head
    while temp:
        s += str(temp.data)
        temp = temp.next

    s = str(int(s) + 1)
    dummy = Node(-1)
    curr = dummy
    for i in s:
        curr.next = Node(int(i))
        curr = curr.next
    return dummy.next

def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

def solution2(head):
    curr = head
    carry = 1
    temp = head
    last = None
    while curr:
        sums = carry + curr.data
        carry = 1 if sums >= 10 else 0
        curr.data  = sums % 10
        last = curr
        curr = curr.next
    if carry > 0:
        last.next = Node(carry)
    return temp

def add(head):
    head = reverse(head)
    result = solution2(head)
    return reverse(result)






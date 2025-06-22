# Odd even linked list
from os import device_encoding


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

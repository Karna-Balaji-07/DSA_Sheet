# add two numbers

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def solution1(head1, head2):
    s1= ""
    s2 = ""
    curr = head1
    temp = head2
    while curr:
        s1 += str(curr.data)
        curr = curr.next
    while temp:
        s2  +=str(temp.data)
        temp = temp.next

    i = int(s1[::-1])
    j = int(s2[::-1])
    sums = str(i+j)
    dummy = Node(-1)
    curr = dummy
    for i in sums:
        curr.next = Node(int(i))
        curr = curr.next
    return dummy.next

def solution2(head1, head2):
    dummy = Node()
    curr = dummy
    carry = 0
    while head1 or head2 or carry:
        num1 = head1.data if head1 else 0
        num2 = head2.data if head2 else 0
        sums = num1+num2+carry
        carry = sums // 10
        sums %= 10
        curr.next = Node(sums)
        curr = curr.next
        num1 = num1.next if num1 else None
        num2 - num2.next if num2 else None

    return dummy.next


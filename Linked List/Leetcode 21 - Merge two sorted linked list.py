# merge two sorted linked list

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def solution1(list1, list2):
    dummy = Node(-1)
    curr= dummy
    while list1 and list2:
        if list1.data < list2.data:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next

def solution2(list1, list2):
    arr = []
    temp1 = list1
    temp2 = list2
    while temp1:
        arr.append(temp1.data)
        temp1 = temp1.next
    while temp2:
        arr.append(temp2.data)
        temp2 = temp2.next

    arr.sort()
    dummy = Node(-1)
    curr = dummy
    for i in range(len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return dummy.next


def printll(head):
    while head:
        print(head.data,end=" ")
        head = head.next

# First linked list: 5 -> 10 -> 15 -> 40
head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(15)
head1.next.next.next = Node(40)

# Second linked list: 2 -> 3 -> 20
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(20)

result = solution2(head1, head2)
printll(result)


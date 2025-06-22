class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def solution1(head1, head2):
    curr1 = head1
    curr2 = head2
    if not curr1 or not curr2:
        return None
    while curr1 != curr2:
        if curr1 is None:
            curr1 = head2
        else:
            curr1 = curr1.next
        if curr2 is None:
            curr2 = head1
        else:
            curr2 = curr2.next
    return curr1

def solution2(headA, headB):
    s = set()
    temp = headA
    while temp:
        s.add(temp.data)
        temp = temp.next

    while headB:
        if headB in s:
            return headB
        headB = headB.next

    return None

 # creation of first list: 10 -> 15 -> 30
head1 = Node(10)
head1.next = Node(15)
head1.next.next = Node(30)

# creation of second list: 3 -> 6 -> 9 -> 15 -> 30
head2 = Node(3)
head2.next = Node(6)
head2.next.next = Node(9)

# 15 is the intersection point
head2.next.next.next = head1.next

intersect = solution2(head1, head2)
print(intersect )
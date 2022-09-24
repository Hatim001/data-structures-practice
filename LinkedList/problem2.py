"""

Linked List Reversal

Problem
Write a function to reverse a Linked List in place. The function will take in the head of the 
list as input and return the new head of the list.

"""

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.next = None

def reverse(node: Node):
    
    current = node
    previous = None
    nxt = None

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(a.next.value, "=>", b.next.value, "=>", c.next.value, "=>", (d.next and d.next.value) or None)

reverse(a)

print(d.next.value, "=>", c.next.value, "=>", b.next.value, "=>", (a.next and a.next.value) or None)
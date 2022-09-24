"""

Singly Linked List Cycle Check
Problem
Given a singly linked list, write a function which takes in the first node in a singly linked list and 
returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is also 
sometimes known as a circularly linked list.

"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.next != None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker1 == marker2:
            return True
    
    return False



a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

print(cycle_check(a))
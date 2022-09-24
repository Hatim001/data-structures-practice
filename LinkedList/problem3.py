"""

Linked List Nth to Last Node

Problem Statement
Write a function that takes a head node and an integer value n and then 
returns the nth to last node in the linked list.

"""

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.next = None

def nth_to_last_node(n, head: Node) -> Node:

    left = head
    right = head

    for _ in range(n):
        if right is None:
            raise LookupError("List doesn't contain the node!!")
        right = right.next

    while right != None:
        left = left.next
        right = right.next

    return left


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(4, a)
print(target_node.value)
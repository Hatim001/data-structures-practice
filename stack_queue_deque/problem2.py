"""
Implement a Queue - Using Two Stacks

Given the Stack class below, implement a Queue class using two stacks! Note, 
this is a "classic" interview problem. Use a Python list data structure as your Stack.
"""

from stack import Stack


class Queue2Stacks(object):

    def __init__(self):
        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, element):
        self.in_stack.push(element)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

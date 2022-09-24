



You are given a linked list and an integer k. You have to swap the kth node from the beginning and the kth node from the end.

list => 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
k = 3
ans => 1 -> 2 -> 5 -> 4 -> 3 -> 6 -> 7 -> None

Final goal is to get to a solution which doesn't involve swapping the values


class Node:
    def __init__(self):
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None

    def add_multi_values(self, values):
        self.head = Node()
        self.head = self.tail = values[0]
        for i in range(len(values)):
            

    def swapItems(self, pos=None):
        # get the count of the item
        count = len(LinkedList)
        
        # loop through the linked list
        head = self.head
        itr = 0
        start = None
        end = None
        while head.next != None:
            # remove the store the kth and len-kth item
            if itr == (pos-1)-1:
                start = head.next
                head = head.next.next
            elif itr == count - (pos - 1):
                end = head.next
                head = head.next.next
            head = head.next
            itr += 1
        
        head = self.head
        itr = 0
        while head.next != None:
            if itr == (pos-1):
                nextItem = head
                head = end
                end.next = nextItem
            elif itr == count - (pos):
                nextItem = head
                head = start
                start.next = nextItem



        # reinsert it again







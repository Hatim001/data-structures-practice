class Node:
    def __init__(self, val=None, nextNode=None) -> None:
        self.val = val
        self.next = nextNode


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    def insertAtHead(self, val):
        #  create new node
        new_node = Node(val)

        # assign next of new node to current head
        new_node.next = self.head

        # assign head as new node
        self.head = new_node

        # increment size (optional if you want to maintain size)
        self.size += 1

    def insertAtEnd(self, val):
        #  create new node
        new_node = Node(val)
        
        # check whether head is none
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        # loop through till the last element
        while curr.next != None:
            curr = curr.next

        # assign the element to the last node
        curr.next = new_node
        self.size += 1

    def deleteNode(self, position):
        
        # if nothing exist
        if self.head is None:
            return

        temp = self.head
        if position == 0:
            self.head = self.head.next
            return temp

        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None or temp.next is None:
            return
 
        next = temp.next.next
        temp.next = next
        return

    def display(self):

        curr = self.head
        while curr != None:
            print("{0} => {1}".format(curr.val,
                  "None" if curr.next is None else ""), end="")
            curr = curr.next


obj = SinglyLinkedList()
obj.insertAtHead(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.display()
print(obj.size)


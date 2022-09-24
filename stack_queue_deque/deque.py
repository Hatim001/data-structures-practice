from typing import Any
from base import BaseClass


class Deque(BaseClass):
    """ 
    Implements Deque Data Structure
    Operations - 
    1. Check if its empty
    2. Add to both front and rear
    3. Remove from front and rear
    4. Check the size
    """

    def __init__(self) -> None:
        super().__init__(package="Deque")

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self) -> Any:
        return self.isEmpty() or self.items.pop()

    def removeRear(self) -> Any:
        return self.isEmpty() or self.items.pop(0)
    
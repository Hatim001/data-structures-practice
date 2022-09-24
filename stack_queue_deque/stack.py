from typing import Any
from base import BaseClass


class Stack(BaseClass):
    """ 
    Implements Stack Data Structure
    Operations - 
    1. Check if its empty
    2. Push a new Item
    3. Pop an Item
    4. Peek at the top item
    5. Return the size
    """

    def __init__(self) -> None:
        super().__init__(package="Stack")

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        return self.isEmpty() or self.items.pop()

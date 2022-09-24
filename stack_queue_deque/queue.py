from typing import Any
from base import BaseClass


class Queue(BaseClass):
    """ 
    Implements Queue Data Structure
    Operations - 
    1. Check if its empty
    2. Enqueue
    3. Dequeue
    4. Return the size
    """

    def __init__(self) -> None:
        super().__init__(package="Queue")

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        return self.isEmpty() or self.items.pop(0)

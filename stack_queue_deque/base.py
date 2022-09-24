from typing import Any


class BaseClass(object):
    """ handles common operation across stack, queue & deque """

    def __init__(self, package) -> None:
        self.items = []
        self.package = package

    def isEmpty(self) -> bool:
        return self.items == []

    def peek(self) -> Any or None:
        return self.isEmpty() or self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def display(self) -> None:
        print(self.items)

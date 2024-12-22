from typing import List

class Stack:
    def __init__(self, capacity: int) -> None:
        self.stack: List[int] = []
        self.capacity: int = capacity
        self.length: int = self.stack.__len__()

    def Push(self, value: int) -> None:
        if self.length == self.capacity:
            return None
        self.stack.insert(0, value)

    def Pop(self):
        if self.length == 0:
            return None
        return self.stack.pop(0)

    def Peek(self):
        if self.length == 0:
            return None
        return self.stack[0]

    def setCapacity(self, capacity) -> None:
        self.capacity = capacity

    def getLength(self) -> int:
        return self.stack.__len__()

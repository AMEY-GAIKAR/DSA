class Stack:
    def __init__(self, capacity: int) -> None:
        self.stack: list = []
        self.capacity: int = capacity

    def Push(self, value) -> None:
        if self.getCapacity() == self.capacity:
            return None
        self.stack.insert(0, value)

    def Pop(self):
        if self.getCapacity() == 0:
            return None
        return self.stack.pop(0)

    def Peek(self):
        if self.getCapacity() == 0:
            return None
        return self.stack[0]

    def getCapacity(self) -> int:
        return self.stack.__len__()

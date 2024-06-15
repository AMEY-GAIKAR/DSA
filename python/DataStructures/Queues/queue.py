from typing import List

class Queue:
    def __init__(self, capacity: int) -> None:
        self.queue: List[int] = []
        self.capacity: int = capacity

    def Append(self, value: int) -> None:
        if self.getLength() == self.capacity:
            return None
        self.queue.append(value)

    def Prepend(self, value: int) -> None:
        if self.getLength() == self.capacity:
            return None
        self.queue.insert(0, value)

    def LPop(self):
        if self.getLength() == 0:
            return None
        return self.queue.pop(0)
    
    def RPop(self):
        if self.getLength() == 0:
            return None
        return self.queue.pop(-1)

    def getLength(self) -> int:
        return self.queue.__len__()

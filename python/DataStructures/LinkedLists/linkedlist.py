from typing import List

class Node:
    def __init__(self, key: int, next) -> None:
        self.key: int = key
        self.next: Node = next

class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head: Node = head
        self.length: int = 0

    def Traverse(self) -> List[int]:
        elements: List[int] = []
        current: Node = self.head
        while current != None:
            elements.append(current.key)
            current = current.next
        return elements

    def Search(self, val: int) -> bool:
        current: Node = self.head
        while current != None:
            if current.key == val:
                return True
            current = current.next
        return False

    def __len__(self) -> int:
        self.length = 0
        current: Node = self.head
        while current != None:
            self.length += 1
            current = current.next
        return self.length

    def Append(self, node: Node) -> None:
        if not self.head:
            self.head = node
        else:
            current: Node = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def Prepend(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def DeleteFirst(self) -> None:
        next: Node = self.head.next
        self.head = next

    def DeleteLast(self) -> None:
        current: Node = self.head
        prev: Node = None
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None

    def Reverse(self) -> None:
        current: Node = self.head
        prev: Node | None = None
        while current.next != None:
            temp: Node = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        self.head = current

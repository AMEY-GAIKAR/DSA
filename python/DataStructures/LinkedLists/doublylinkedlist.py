from typing import List

class Node:
    def __init__(self, key: int, next, prev) -> None:
        self.key: int = key
        self.next: Node = next
        self.prev: Node = prev

class DoublyLinkedList:
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
            node.prev = current

    def Prepend(self, node: Node) -> None:
        node.next = self.head
        self.head.prev = node
        self.head = node

    def InsertBefore(self, val: int, node: Node) -> None:
        current: Node = self.head
        if current.key == val:
            self.Prepend(node)
            return None
        while current != None:
            if current.key == val:
                node.next = current
                node.prev = current.prev
                current.prev.next = node
                current.prev = node
                return None
            current = current.next
        return None

    def InsertAfter(self, val: int, node: Node) -> None:
        current: Node = self.head
        while current != None:
            if current.key == val:
                if current.next:
                    current.next.prev = node
                    node.next = current.next
                current.next = node
                node.prev = current.prev
                return None
            current = current.next
        return None

    def InsertAt(self, position: int, node: Node) -> None:
        if position == 0:
            self.Prepend(node)
            return None
        current: Node = self.head.next
        index: int = 1
        while current:
            if index == position:
                node.next = current
                node.prev = current.prev
                current.prev.next = node
                current.prev = node
                return None
            index += 1
            current = current.next
        if position == index:
            self.append(node)
        return None

    def DeleteFirst(self) -> None:
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None
        next: Node = self.head.next
        self.head.next = None
        self.head = next
        self.head.prev = None

    def DeleteLast(self) -> None:
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None
        current: Node = self.head
        while current.next != None:
            current = current.next
        prev: Node = current.prev
        current.prev = None
        prev.next = None

    def DeleteVal(self, val) -> None:
        if self.head.key == val:
            self.DeleteFirst()
        current: Node = self.head.next
        while current != None:
            if current.key == val:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            current = current.next

    def Reverse(self) -> None:
        current: Node | None = self.head
        prev: Node | None = None
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        self.head = prev.prev

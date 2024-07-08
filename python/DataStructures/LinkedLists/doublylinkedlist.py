from typing import List

class Node:
    def __init__(self, key: int, next = None, prev = None) -> None:
        self.key: int = key
        self.next: Node | None = next
        self.prev: Node | None = prev

class DoublyLinkedList:
    def __init__(self, head: Node) -> None:
        self.head: Node = head
        self.length: int = self.__len__()

    def traverse(self) -> List[int]:
        elements: List[int] = []
        current: Node = self.head
        while current != None:
            elements.append(current.key)
            current = current.next
        return elements
    
    def search(self, val: int) -> bool:
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

    def append(self, node: Node) -> None:
        if not self.head:
            self.head = node
        else:
            current: Node = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current

    def prepend(self, node: Node) -> None:
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertBefore(self, val: int, node: Node) -> None:
        current: Node = self.head
        if current.key == val:
            self.prepend(node)
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

    def insertAfter(self, val: int, node: Node) -> None:
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

    def insertAt(self, position: int, node: Node) -> None:
        if position == 0:
            self.prepend(node)
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

    def deleteFirst(self) -> None:
        if not self.head:
            return None
        if not self.head.next:
            self.head = None
            return None
        next: Node = self.head.next
        self.head.next = None
        self.head = next
        self.head.prev = None

    def deleteLast(self) -> None:
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

    def deleteVal(self, val) -> None:
        if self.head.key == val:
            self.deleteFirst()
        current: Node = self.head.next
        while current != None:
            if current.key == val:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            current = current.next

    def reverse(self) -> None:
        current: Node | None = self.head
        prev: Node | None = None
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
        self.head = prev.prev

A = Node(1)
B = Node(2)
C = Node(1)
D = Node(4)
E = Node(5)
F = Node(1)
G = Node(1)
dll = DoublyLinkedList(A)
dll.append(B)
dll.append(C)
dll.append(D)
dll.append(E)
dll.append(F)
print(dll.traverse())
dll.deleteVal(1)
print(dll.traverse())

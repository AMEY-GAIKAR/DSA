from typing import List

class Node:
    def __init__(self, key: int, next = None) -> None:
        self.key: int = key
        self.next: Node | None = next

class LinkedList:
    def __init__(self, head: Node) -> None:
        self.head: Node = head
        self.length: int = 0

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

    def prepend(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def deleteFirst(self) -> Node:
        next: Node = self.head.next
        self.head.next = None
        self.head = next
        return next

    def deleteLast(self) -> Node:
        current: Node = self.head
        prev: Node = None
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None
        return current

    def reverse(self) -> None:
        current: Node = self.head
        prev: Node | None = None
        while current.next != None:
            temp: Node = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        self.head = current
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.next = B
B.next = C
C.next = D
D.next = E

ll = LinkedList(A)
print(ll.traverse())

from typing import List

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverseList(head: ListNode) -> list[int]:
    """
    Set a pointer(current) to the head and iteratively assign the pointer
    to the next node until the end of the list is reached ie. a null 
    pointer is set to current.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current: ListNode = head
    elements: list[int] = []
    while current != None:
        elements.append(current.val)
        current = current.next
    return elements

def reverseList(head) -> ListNode:
    current: ListNode = head
    prev: ListNode | None = None
    while current.next != None:
        temp: ListNode = current.next
        current.next = prev
        prev = current
        current = temp
    current.next = prev
    return current 

def middleNode(head: ListNode) -> ListNode:
    current: ListNode = head
    middle: ListNode = head
    l: int = -1
    while current.next != None:
        l += 1
        current = current.next
        if l % 2 == 0:
            middle = middle.next
    return middle

def middleNode_II(head: ListNode) -> ListNode | None:
    if not head:
        return None
    fast: ListNode = head
    slow: ListNode = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def deleteMiddle(head: ListNode) -> ListNode:
        current: ListNode = head
        middle: ListNode = head
        prev: ListNode = head
        l: int = -1
        if current.next == None:
            return None
        while current.next != None:
            l += 1
            current = current.next
            if l % 2 == 0:
                prev = middle
                middle = middle.next
        prev.next = middle.next
        return head

def removeDuplicates(head: ListNode) -> ListNode:
    current: ListNode = head
    prev: ListNode = head
    currVal: int = head.val
    while current != None:
        if current.val == currVal:
            prev.next = current.next
            currVal = current.val
        else:
            currVal = current.val
            prev = current
        current = current.next
    return head

def removeElements(head: ListNode, val: int) -> ListNode:
    current: ListNode | None = head
    prev: ListNode | None = None
    while current != None:
        if current.val == val:
            if not prev:
                head = current.next
            else:
                prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return head

def hasCycle(head: ListNode) -> bool:
    fast: ListNode = head
    slow: ListNode = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode | None:
    p1: ListNode | None = headA
    while p1:
        p2: ListNode | None = headB
        while p2:
            if p1 == p2:
                return p1
            p2 = p2.next
        p1 = p1.next
    return None

def getIntersectionNodeII(headA: ListNode, headB: ListNode) -> ListNode | None:
    check: set[ListNode] = set()
    current: ListNode | None = headA
    while current:
        check.add(current)
        current = current.next
    current = headB
    while current:
        if current in check:
            return current
        current = current.next
    return None

def removeNthNode(head: ListNode, n: int) -> ListNode:
    fast: ListNode = head
    slow: ListNode = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head
    while fast.next:
        fast = fast.next
        slow = slow.next
    if not fast.next:
        return head.next
    slow.next = slow.next.next
    return head

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head:
        return None
    newHead: ListNode = head
    if head.next:
        newHead = reverseListRecursive(head.next)
        head.next.next = head
    head.next = None
    return newHead

def palindromeLL(head: ListNode):
    rev : ListNode = reverseList(middleNode_II(head))
    curr: ListNode = head
    while curr.next:
        if curr.val != rev.val:
            return False
        rev = rev.next
        curr = curr.next
    return True

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
        return head
    current: ListNode = head
    length: int = 0
    while current:
        length += 1
        current = current.next
    if k == length:
        return head
    places: int = k % length
    if places == 0:
        return head
    last: ListNode = head
    for _ in range(length-places-1):
        last = last.next
    newHead: ListNode = last.next
    last.next = None
    if length == 1:
        return head
    current = newHead
    while current.next:
        current = current.next
    current.next = head
    return newHead

def getDecimalValue(head: ListNode) -> int:
    current: ListNode = head
    elements: List[int] = []
    decimal: int = 0
    power: int = 1
    while current:
        elements.append(current.val)
        current = current.next
    print(elements)
    for i in range(len(elements)-1, -1, -1):
        decimal += elements[i] * power
        power *= 2
    return decimal

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    current: ListNode = head
    prev: ListNode | None = None
    count: int = 0
    while k > count:
        temp: ListNode = current.next
        current.next = prev
        prev = current
        current = temp
        count += 1
    new: ListNode = current.next
    current.next = prev
    tail: ListNode = head
    tail.next = new
    return current

if __name__ == "__main__":
    A = ListNode(1)
    B = ListNode(0)
    C = ListNode(1)
    D = ListNode(1)
    E = ListNode(0)
    F = ListNode(0)
    A.next = B
    B.next = C
    C.next = D 
    D.next = E
    E.next = F
    # G = ListNode(6)
    # H = ListNode(1)
    # I = ListNode(8)
    # J = ListNode(4)
    # K = ListNode(5)
    # F.next = G
    # G.next = B
    # H.next = I
    # I.next = J
    # J.next = K 
    print(traverseList(A))
    print(getDecimalValue(A))
    # print(traverseList(reverseKGroup(A, 2)))

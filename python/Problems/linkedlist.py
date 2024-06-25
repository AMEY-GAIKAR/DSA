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

def reverseList(head):
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

if __name__ == "__main__":
    A = ListNode(4)
    B = ListNode(1)
    C = ListNode(8)
    D = ListNode(4)
    E = ListNode(5)
    A.next = B
    # B.next = C
    # C.next = D 
    # D.next = E
    # F = ListNode(5)
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
    print(traverseList(removeNthNode(A, 2)))

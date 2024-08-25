from typing import List

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

def getLength(head: ListNode) -> int:
    count: int = 0
    current: ListNode | None = head
    while current:
        count += 1
        current = current.next
    return count

def searchKey(head: ListNode, key: int) -> bool:
    current: ListNode | None = head
    while current:
        if current.val == key:
            return True
        current = current.next
    return False

def insertAtEnd(head: ListNode, val: int) -> ListNode:
    node: ListNode = ListNode(val=val)
    if not head:
        return node
    current: ListNode = head
    while current.next:
        current = current.next
    current.next = node
    return head

def arrayToLinkedList(nums: List[int]) -> ListNode | None:
    if len(nums) == 0:
        return None
    head: ListNode = ListNode(val=nums[0])
    prev: ListNode = head
    for i in range(1, len(nums)):
        node: ListNode = ListNode(val=nums[i])
        prev.next = node
        prev = node
    return head

def traverseList(head: ListNode) -> list[int]:
    """
    Set a pointer(current) to the head and iteratively assign the pointer
    to the next node until the end of the list is reached ie. a null 
    pointer is set to current.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current: ListNode | None = head
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
    l: int = 0
    while current.next != None:
        l += 1
        current = current.next
        if l % 2 == 0:
            middle = middle.next
    if l % 2 == 0:
        return middle
    return middle.next

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

def palindromeLLI(head: ListNode) -> bool:
    elements: List[int] = []
    current: ListNode = head
    while current:
        elements.append(current.val)
        current = current.next
    i: int = 0
    j: int = len(elements) - 1
    while i < j:
        if elements[i] != elements[j]:
            return False
        i += 1
        j -= 1
    return True

def palindromeLLII(head: ListNode):
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
    for i in range(len(elements)-1, -1, -1):
        decimal += elements[i] * power
        power *= 2
    return decimal

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry: int = 0
    result: ListNode = ListNode(0)
    tail: ListNode = result
    c1: ListNode = l1
    c2: ListNode = l2
    while c1 and c2:
        sum = c1.val + c2.val + carry
        n = ListNode(val=(sum)%10)
        tail.next = n
        tail = n
        carry = sum//10
        c1 = c1.next
        c2 = c2.next
    if not c1 and not c2 and carry == 1:
        tail.next = ListNode(1)
    if c1:
        while c1:
            sum = c1.val + carry
            n = ListNode(val=(sum)%10)
            carry = sum//10
            tail.next = n
            tail = n
            c1 = c1.next
        if carry == 1:
            tail.next = ListNode(1)
    elif c2:
        while c2:
            sum = c2.val + carry
            n = ListNode(val=(sum)%10)
            carry = sum//10
            tail.next = n
            tail = n
            c2 = c2.next
        if carry == 1:
            tail.next = ListNode(1)
    return result.next

if __name__ == "__main__":
    print()

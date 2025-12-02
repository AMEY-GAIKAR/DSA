from typing import List


class ListNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


def addNodeAtIndex(head: ListNode, position: int, val: int) -> ListNode:
    node: ListNode = ListNode(val=val)
    current: ListNode = head
    for _ in range(position):
        current = current.next
    node.next = current.next
    if current.next:
        current.next.prev = node
    current.next = node
    node.prev = current
    return head


def deleteNodeAtIndex(head: ListNode, position: int) -> ListNode | None:
    current: ListNode = head
    if position == 1 and not head.next:
        return None
    if position == 1:
        head = head.next
        head.prev = None
        return head
    for _ in range(position - 1 - 1):
        current = current.next
    if not current.next or not current.next.next:
        current.next = None
        return head
    current.next.next.prev = current
    current.next = current.next.next
    return head


def reverseDLL(head: ListNode) -> ListNode:
    if not head.next:
        return head
    current: ListNode = head
    prev: ListNode | None = None
    while current:
        prev = current.prev
        current.prev = current.next
        current.next = prev
        current = current.prev
    return prev.prev


def constructDLL(nums: List[int]) -> ListNode:
    head: ListNode = ListNode(val=nums[0])
    prev: ListNode = head
    for i in range(1, len(nums)):
        node: ListNode = ListNode(val=nums[i])
        node.prev = prev
        prev.next = node
        prev = node
    return head

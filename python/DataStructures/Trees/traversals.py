from typing import List

class TreeNode:
    def __init__(self, value: int, right = None, left = None) -> None:
        self.value: int = value
        self.right: TreeNode | None = right
        self.left: TreeNode | None = left
                
def PreorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    print(node.value)
    if node.left:
        PreorderTraversalRecursive(node.left)
    if node.right:
        PreorderTraversalRecursive(node.right)

def InorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    if node.left:
        InorderTraversalRecursive(node.left)
    print(node.value)
    if node.right:
        InorderTraversalRecursive(node.right)

def PostorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    if node.left:
        PostorderTraversalRecursive(node.left)
    if node.right:
        PostorderTraversalRecursive(node.right)
    print(node.value)

def LevelorderTraversal(node: TreeNode) -> List[int]:
    if not node:
        return []
    elements: List[int] = []
    queue: List[TreeNode]= []
    queue.append(node)
    while queue.__len__() != 0:
        current: TreeNode = queue.pop(0)
        elements.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return elements 

def BreadthFirstTraversal(node: TreeNode) -> List[List[int]] | None:
    if not node:
        return None
    elements: List[List[int]] = []
    queue: List[TreeNode] = []
    queue.append(node)
    while queue.__len__() != 0:
        base: int = len(queue)
        current: List[int] = []
        for _ in range(base):
            node = queue.pop(0)
            current.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        elements.append(current)
    return elements

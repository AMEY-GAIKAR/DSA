from typing import List

class TreeNode:
    def __init__(self, value: int, right = None, left = None) -> None:
        self.value: int = value
        self.right: TreeNode | None = right
        self.left: TreeNode | None = left
                
def preorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    print(node.value)
    if node.left:
        preorderTraversalRecursive(node.left)
    if node.right:
        preorderTraversalRecursive(node.right)

def inorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    if node.left:
        inorderTraversalRecursive(node.left)
    print(node.value)
    if node.right:
        inorderTraversalRecursive(node.right)

def postorderTraversalRecursive(node: TreeNode) -> None:
    if not node:
        return None
    if node.left:
        postorderTraversalRecursive(node.left)
    if node.right:
        postorderTraversalRecursive(node.right)
    print(node.value)

def levelorderTraversal(node: TreeNode) -> List[int]:
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

def breadthFirstTraversal(node: TreeNode) -> List[List[int]] | None:
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

if __name__ == "__main__":
    A = TreeNode(20)
    B = TreeNode(9)
    C = TreeNode(5)
    D = TreeNode(12)
    E = TreeNode(11)
    F = TreeNode(14)
    G = TreeNode(25)
    A.left = B
    A.right = G
    B.left = C
    B.right = D
    D.left = E
    D.right = F

    print(inorderTraversalRecursive(A))

from typing import List

class TreeNode:
    def __init__(self, value: int, right = None, left = None) -> None:
        self.value: int = value
        self.right: TreeNode | None = right
        self.left: TreeNode | None = left

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

def treeHeight(node: TreeNode) -> int:
    if not node:
        return 0
    height: int = 0
    queue: List[TreeNode] = []
    queue.append(node)
    while queue.__len__() != 0:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1
    return height

def maxDepth(node: TreeNode) -> int:
    def dfs(node: TreeNode, depth: int) -> int:
        if not node:
            return depth
        return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
    return dfs(node, 0)

def BSTInsert(node: TreeNode, x: int):
    if node.value >= x:
        if not node.left:
            node.left = TreeNode(x)
        else:
            BSTInsert(node.left, x)
    elif node.value <= x:
        if not node.right:
            node.right = TreeNode(x)
        else:
            BSTInsert(node.right, x)

def isSymmetric(root: TreeNode) -> bool:
    def helper(node1: TreeNode, node2: TreeNode) -> bool:
        if not node1 or not node2:
            return True
        return node1.value == node2.value and helper(node1.left, node2.right) and helper(node1.right, node2.left)
    if not root:
        return True
    if not root.left and not root.right:
        return True
    return helper(root.left, root.right)

if __name__ == "__main__":
    A = TreeNode(10)
    print()

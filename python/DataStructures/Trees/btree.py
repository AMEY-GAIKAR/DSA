#     a
#    / \
#   b   c
#  /\   /\
# d  e f  g
#
#     10
#     /\
#   5   16
#  /\   /\
# 4  7 13 20

class TreeNode(object):
    def __init__(self, value):
        self.value = value
                
    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

A = TreeNode(10)
B = TreeNode(5)
C = TreeNode(16)
D = TreeNode(4)
E = TreeNode(7)
F = TreeNode(13)
G = TreeNode(20)

A.setLeft(B)
A.setRight(C)
B.setLeft(D)
B.setRight(E)
C.setLeft(F)
C.setRight(G)
D.setLeft(None)
D.setRight(None)
E.setLeft(None)
E.setRight(None)
F.setLeft(None)
F.setRight(None)
G.setLeft(None)
G.setRight(None)

def depthFirstTraversal(node):
    if node == None:
        return []
    
    stack = []
    nodes = []

    stack.append(node)

    while (len(stack) != 0):
        current = stack.pop()
        nodes.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return nodes

def breadthFirstTraversal(node):
    if node == None:
        return []
    
    queue = []
    nodes = []
    
    queue.append(node)

    while (len(queue) != 0):
        current = queue.pop(0)
        nodes.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return nodes

def depthFirstSearch(node, value):
    if node == None:
        return False
    
    stack = []

    stack.append(node)
    while (len(stack) != 0):
        current = stack.pop()
        if current.value == value:
            return True
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return False

def breadthFirstSearch(node, value):
    if node == None:
        return False
    
    queue = []

    queue.append(node)
    while (len(queue) != 0):
        current = queue.pop(0)
        if current.value == value:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

def depthFirstSearchRecursive(node, value):
    if node == None:
        return False
    if node.value == value:
        return True
    return depthFirstSearchRecursive(node.left, value) or depthFirstSearchRecursive(node.right, value)
    
def treeSumRecursive(node):
    if node == None:
        return 0
    return node.value + treeSumRecursive(node.left) + treeSumRecursive(node.right) 

def treeSumDFS(node):
    if node == None:
        return 0
    
    stack = []
    sum = 0

    stack.append(node)
    while (len(stack) != 0):
        current = stack.pop()
        sum += current.value
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return sum

def treeSumBFS(node):
    if node == None:
        return False

    queue = []
    sum = 0

    queue.append(node)
    while (len(queue) != 0):
        current = queue.pop(0)
        sum += current.value
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum

if __name__ == "__main__":
    print(depthFirstTraversal(A))

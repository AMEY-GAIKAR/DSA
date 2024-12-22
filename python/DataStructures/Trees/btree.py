class TreeNode(object):
    def __init__(self, value):
        self.value = value
                
    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

def DepthFirstTraversal(node):
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

def BreadthFirstTraversal(node):
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

def DepthFirstSearch(node, value):
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

def BreadthFirstSearch(node, value):
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

def DepthFirstSearchRecursive(node, value):
    if node == None:
        return False
    if node.value == value:
        return True
    return DepthFirstSearchRecursive(node.left, value) or DepthFirstSearchRecursive(node.right, value)
    
def TreeSumRecursive(node):
    if node == None:
        return 0
    return node.value + TreeSumRecursive(node.left) + TreeSumRecursive(node.right) 

def TreeSumDFS(node):
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

def TreeSumBFS(node):
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

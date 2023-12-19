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

class Node(object):
    def __init__(self, value):
        self.value = value
                
    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

A = Node(10)
B = Node(5)
C = Node(16)
D = Node(4)
E = Node(7)
F = Node(13)
G = Node(20)

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

def depthFirstSearch(node):
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

print(depthFirstSearch(A))

def inorder(n):
    if n == None:
        return
    inorder(n.left)
    print(n.data, end = ' ')
    inorder(n.right)

def postorder(n):
    if n == None:
        return
    postorder(n.left)
    postorder(n.right)
    print(n.data, end = ' ')

def preorder(n):
    if n == None:
        return
    print(n.data, end = ' ')
    preorder(n.left)
    preorder(n.right)

class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n1 = treeNode(1)
n2 = treeNode(2)
n3 = treeNode(3)
n4 = treeNode(4)
n5 = treeNode(5)
n6 = treeNode(6)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6

preorder(n1)

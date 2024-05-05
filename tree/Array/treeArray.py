tree = ['0', 'a', 'b', 'c', 'd', 'e', '0', 'f', 'g', '0', 'h', 'i', '0', '0', 'j', '0']


class arrTree():
    def __init__(self, a):
        self.tree = a
        self.tree[0] = len(self.tree)

    def getRightChild(self, n):
        if((n*2+1)>= self.tree[0]):
            return -1
        return n*2+1
        
    def getLeftChild(self, n):
        if(n*2 >= self.tree[0]):
            return -1
        return n*2

    def preorder(self, index):
        if(self.tree[index] != '0' and index>0):
            print(self.tree[index], end = ' ')
            self.preorder(self.getLeftChild(index))
            self.preorder(self.getRightChild(index))
    
    def postorder(self, index):
        if(self.tree[index] != '0' and index>0):
            self.postorder(self.getLeftChild(index))
            self.postorder(self.getRightChild(index))
            print(self.tree[index], end = ' ')

    def inorder(self, index):
        if(self.tree[index] != '0' and index>0):
            self.inorder(self.getLeftChild(index))
            print(self.tree[index], end = ' ')
            self.inorder(self.getRightChild(index))

arr = arrTree(tree)
print("preorder : ", end = ' ')
arr.preorder(1)
print()
print("postorder : ", end = ' ')
arr.postorder(1)
print()
print("inorder : ", end = ' ')
arr.inorder(1)
print()
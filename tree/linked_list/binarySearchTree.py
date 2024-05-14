
class tree():
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

class bst():
    def __init__(self):
        self.root = None
        
    def bstSearch(self, key):
        current = self.root
        morepast = None

        if(current == None): #When root node is None
            return False, None

        while(True):
            past = current # past is for def bstInsert
            if(current.key == key):  #Found a in tree
                return True, past, morepast
            if(key<current.key): #When a is smaller than current.key
                morepast = current
                current = current.left #current moved to left
            elif(key>current.key): #when a is bigger than current.key
                morepast = current
                current = current.right #current moved to right
            
            if(current == None): #current is not exist, then tree dosen't have a
                return False, past #Can't find a, then return past for bstInsert

    def bstInsert(self, key, data = None):
        #current[0] means whether or not tree have a
        #current[1] is past in def bstSearch
        current = self.bstSearch(key)
        if(current[1] == None): #when tree has no root
            data = input("Please enter "+str(key)+" key data : ")
            self.root = tree(key,data)
            return
        if(current[0] == True): #When find a in tree
            print("It already has " + str(key) + ", Please update data")
            data = input("Please enter "+str(key)+" key data : ")
            current[1].data = data
            return
        
        if(data == None):
            data = input("Please enter "+str(key)+" key data : ")
            temp = tree(key,data) #When tree doesn't have a
            if(key>current[1].key): #Put a in the right place
                current[1].right = temp
            elif(key<current[1].key):
                current[1].left = temp
        else:
            temp = tree(key,data)
            if(key>current[1].key): #Put a in the right place
                current[1].right = temp
            elif(key<current[1].key):
                current[1].left = temp

    
    def bstDelete(self, key): #Delete
        current = self.bstSearch(key)
        if(current[0] == False):
            print("Can't find " + str(key))
        #delete left or right of morepast
        if(current[2].key > current[1].key):
            current[2].left = None
        elif(current[2].key < current[1].key):
            current[2].right = None
        
        #Insert sons of past
        self.bstpreorderForInsert(current[1].left)
        self.bstpreorderForInsert(current[1].right)
        
    def bstpreorderForInsert(self, current):
        if(current == None):
            return
        self.bstInsert(current.key, current.data)
        self.bstpreorderForInsert(current.left)
        self.bstpreorderForInsert(current.right)

    def bstDeleteUpdate(self, key): #update delete
        current = self.bstSearch(key)

        if(current[0] == False):
            print("This tree has no " + str(key))
            return
        
        #node is leaf
        if(current[1].left == None and current[1].right == None):
            if(current[1] == self.root): #When the node Im gonna delete is root has no sons
                self.root = None
                return
            if(current[1].key > current[2].key):
                current[2].right = None
            else:
                current[2].left = None
            return
        #node got a son
        elif(current[1].left != None and current[1].right == None): #node got left, no right
            current[1].key = current[1].left.key
            current[1].data = current[1].left.data
            current[1].right = current[1].left.right
            current[1].left = current[1].left.left
        elif(current[1].right != None and current[1].left == None): #node got right, no left
            current[1].key = current[1].right.key
            current[1].data = current[1].right.data
            current[1].left = current[1].right.left
            current[1].right = current[1].right.right
        #node got two sons
        else:
            node = current[1]
            while(node.right != None):
                parentNode = node
                node = node.right
            parentNode.right = None
            current[1].key = node.key
            current[1].data = node.data

    def bstGetHeight(self):
        print()

    def bstGetDepth(self, node):
        print()
    
    def bstPreOrder(self, current = False):
        if(current == False):
            current = self.root
        if(current == None):
            return
        print(current.key, end = ' ')
        print(current.data)
        self.bstPreOrder(current.left)
        self.bstPreOrder(current.right)


n1 = bst()
keyset = [15,13,11,14,60,44,55,68,65]
for key in keyset:
    n1.bstInsert(key)

n1.bstDeleteUpdate(68)
n1.bstPreOrder()


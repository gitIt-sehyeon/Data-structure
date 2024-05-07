class tree():
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

class bst():
    def __init__(self):
        self.root = None
        
        
    def bstSearch(self, a):
        current = self.root

        if(current == None): #When root node is None
            print("Root node is not exist")
            return False, None

        while(True):
            past = current # past is for def bstInsert
            if(current.key == a):  #Found a in tree
                print("It already has " + str(a) + ", Please update data")
                return True, past
            if(a<current.key): #When a is smaller than current.key
                current = current.left #current moved to left
            elif(a>current.key): #when a is bigger than current.key
                current = current.right #current moved to right
            
            if(current == None): #current is not exist, then tree dosen't have a 
                return False, past #Can't find a, then return past for bstInsert

    def bstInsert(self, a):
        #current[0] means whether or not tree have a
        #current[1] is past in def bstSearch
        current = self.bstSearch(a)
        data = input("Please enter data : ")
        if(current[1] == None): #when tree has no root
            self.root = tree(a,data)
            return
        if(current[0] == True): #When find a in tree
            current[1].data = data
            return
    
        temp = tree(a,data) #When tree doesn't have a
        if(a>current[1].key): #Put a in the right place
            current[1].right = temp
        elif(a<current[1].key):
            current[1].left = temp
        
    def bstPreOrder(self, current):
        if(current == None):
            return
        print(current.key, end = ' ')
        print(current.data)
        self.bstPreOrder(current.left)
        self.bstPreOrder(current.right)


n1 = bst()
n1.bstInsert(15)
n1.bstInsert(13)
n1.bstInsert(50)
n1.bstInsert(11)
n1.bstInsert(14)
n1.bstInsert(50)
n1.bstPreOrder(n1.root)


class tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bstSearch(a):
    global root
    current = root

    if(current == None): #When root node is None
        print("Root node is not exist")
        return None

    while(True): 
        if(current.data == a):  #Found a in tree
            print("It has " + str(a))
            return None #Found a -> return None for bstInsert
        past = current # past is for def bstInsert
        if(a<current.data): #When a is smaller than current.data
            current = current.left #current moved to left
        elif(a>current.data): #when a is bigger than current.data
            current = current.right #current moved to right
        
        if(current == None): #current is not exist, then tree dosen't have a 
            print("It doesn't have " + str(a))
            return past #Can't find a, then return past for bstInsert

def bstInsert(a):
    current = bstSearch(a)
    if(current == None): #When this tree already have a
        print("It already has " + str(a))
        return
    
    print("Insert " + str(a))
    temp = tree(a) #When tree doesn't have a
    if(a>current.data): #Put a in the right place
        current.right = temp
    elif(a<current.data):
        current.left = temp

def bstPreOrder(current):
    if(current == None):
        return
    print(current.data, end = ' ')
    bstPreOrder(current.left)
    bstPreOrder(current.right)

n1 = tree(15)
n2 = tree(11)
n3 = tree(70)
n4 = tree(5)
n1.left = n2
n1.right = n3
n2.left = n4
root = n1

bstInsert(75)
bstPreOrder(n1)
print()
bstInsert(69)
bstPreOrder(n1)

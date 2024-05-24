class maxHeap:
    def __init__(self, arr):
        self.tree = [len(arr)]+arr
    
    def maxInsert(self, data):
        insertIndex = len(self.tree) #Index of node to insert
        self.tree.append(data) #insert node to the last index
        while(True):
            if(self.tree[insertIndex] == self.tree[1]): #When node to insert be the root
                break
            if(self.tree[insertIndex]>self.tree[int(insertIndex/2)]): #Insert node over parent
                self.tree[insertIndex], self.tree[int(insertIndex/2)] = self.tree[int(insertIndex/2)], self.tree[insertIndex]
                insertIndex = int(insertIndex/2)
            else:
                break
    
    def maxDelete(self):
        if len(self.tree) <= 1:
            return None  # If heap is empty
        if len(self.tree) == 2:
            return self.tree.pop()  # Only one element in heap
        
        self.tree[1], self.tree[-1] = self.tree[-1], self.tree[1]
        largest = self.tree.pop()
        n=1

        while(True):
            left = n*2
            right = n*2 + 1
            if(left>=len(self.tree)): #Not exist children
                return largest
            if(right>=len(self.tree)): #only have left child
                if self.tree[left] > self.tree[n]:
                    self.tree[n], self.tree[left] = self.tree[left], self.tree[n]
                return largest
            elif(self.tree[left]>self.tree[right] and self.tree[left]>self.tree[n]): #left child > right child, also bigger than target node
                self.tree[n], self.tree[left] = self.tree[left], self.tree[n]
                n=left
            elif(self.tree[right]>self.tree[left] and self.tree[right]>self.tree[n]): #right child > left child, also bigger than target node
                self.tree[n], self.tree[right] = self.tree[right], self.tree[n]
                n=right
            else:
                return largest
            
    
    def printArr(self):
        for i in range(1, len(self.tree)):
            print(self.tree[i], end=' ')

arr = [18,13,5,12,8]
tree = maxHeap(arr)
tree.maxInsert(19)
tree.maxInsert(21)
tree.maxDelete()
tree.printArr()
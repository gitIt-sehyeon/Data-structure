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
    
    def heapify(self, node):
        left = node*2
        right = node*2+1
        largest = node
        if(left<len(self.tree) and self.tree[largest]<self.tree[left]):
            largest = left
        if(right<len(self.tree) and self.tree[largest]<self.tree[right]):
            largest = right
        
        if(largest != node):
            self.tree[largest], self.tree[node] = self.tree[node], self.tree[largest]
            self.heapify(largest)

    def make_tree_heap(self):
        for i in range(int(len(self.tree)/2), 0, -1):
            print(i)
            self.heapify(i)
    
    def printArr(self):
        for i in range(1, len(self.tree)):
            print(self.tree[i], end=' ')

class minHeap:
    def __init__(self, arr):
        self.tree = [len(arr)]+arr

    def minInsert(self, data):
        insertIndex = len(self.tree)
        self.tree.append(data)
        while(True):
            if(insertIndex == 1):
                return
            if(self.tree[insertIndex]<self.tree[int(insertIndex/2)]):
                self.tree[insertIndex], self.tree[int(insertIndex/2)] = self.tree[int(insertIndex/2)], self.tree[insertIndex] 
                insertIndex = int(insertIndex/2)
            else:
                return

    def minDelete(self):
        if(len(self.tree)<=1):
            return None
        if(len(self.tree)<=2):
            return self.tree.pop()
        
        self.tree[1], self.tree[-1] = self.tree[-1], self.tree[1]
        min = self.tree.pop()

        n = 1
        while(True):
            left = n*2
            right = n*2+1
            if(left >= len(self.tree)):
                return min
            if(right >= len(self.tree)):
                if(self.tree[left]<self.tree[n]):
                    self.tree[left], self.tree[n] = self.tree[n], self.tree[left]
                return min
            if(self.tree[right]<self.tree[left] and self.tree[right] < self.tree[n]):
                self.tree[right], self.tree[n] = self.tree[n], self.tree[right]
                n=right
            elif(self.tree[left]<self.tree[right] and self.tree[left]<self.tree[n]):
                self.tree[left], self.tree[n] = self.tree[n], self.tree[left]
                n=left
            else:
                return min

        print()

    def heapify(self, node):
        left = node*2
        right = node*2+1
        largest = node
        if(left<len(self.tree) and self.tree[largest]>self.tree[left]):
            largest = left
        if(right<len(self.tree) and self.tree[largest]>self.tree[right]):
            largest = right
        
        if(largest != node):
            self.tree[largest], self.tree[node] = self.tree[node], self.tree[largest]
            self.heapify(largest)

    def make_tree_heap(self):
        for i in range(int(len(self.tree)/2), 0, -1):
            print(i)
            self.heapify(i)
    
    def printArr(self):
        for i in range(1, len(self.tree)):
            print(self.tree[i], end = ' ')

arr = [5,8,12,13,18]
tree = maxHeap(arr)
tree.make_tree_heap()
#tree.maxInsert(19)
#tree.maxInsert(21)
#tree.maxDelete()
tree.printArr()
print()

arr2 = [100,80,40,20,15,10,5]
tree2 = minHeap(arr2)
tree2.make_tree_heap()
#tree2.minInsert(8)
#tree2.minDelete()
tree2.printArr()


class MinHeap:
    def __init__(self):
        self.heap = [];

    def push(self, value):
        self.heap.append(value);
        if len(self.heap) > 1:
            self.__heapify_up(len(self.heap)-1)
            

        
    def __heapify_up(self, index):
        parent = (index - 1) // 2
        
        if parent >= 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent],self.heap[index] = self.heap[index] , self.heap[parent]
            self.__heapify_up(parent)
            
    
    def pop(self):
        if len(self.heap) == 0:
            return
        
        root = self.heap[0]
        last =self.heap.pop()
        
        if len(self.heap) >= 1:
            self.heap[0] = last
            self.__heapify_down(0)
        return root
        
    def __heapify_down(self, index):
        smallest = index
        left = (2* index) + 1;
        right = (2 * index) + 2;
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[smallest] , self.heap[index] = self.heap[index] , self.heap[smallest]
            self.__heapify_down(smallest)
    
    def traverse(self):
        print(self.heap)
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

h = MinHeap()
h.push(10)
h.push(4)
h.push(15)
h.push(1)

h.traverse()

print(h.pop()) 
print(h.peek())
h.traverse()  

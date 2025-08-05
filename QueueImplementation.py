class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
        
    def enqueue(self, value):
        self.queue.append(value)
        print(f"Add {value} into Queue \n")
    
    def is_empty(self):
        return True if self.size() == 0 else False

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return
        
        print(f"Remove {self.queue[0]} into Queue \n")
        self.queue.pop(0);
        
    def peek(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return -1
        return self.queue[0]
    
    def traverse(self):
        print(self.queue)
    
    def clear(self):
        while(not self.is_empty()):
            self.queue.pop()
    
    def front(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return -1
        return self.queue[0]
        
    def rear(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return -1
        return self.queue[-1]
        
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.traverse()

q.dequeue()
q.traverse()

print("Front:", q.front())
print("Rear:", q.rear())

q.clear()
q.traverse()

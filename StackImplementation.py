class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
        print(f"{value} pushed into stack \n")
    
    def pop(self):
        val = -1
        if self.is_empty():
            print("Stack is Empty \n")
        else:
            val = self.stack.pop();
        print(f"Popped {val} from stack")
        return val
    
    def top(self):
        val = -1
        if self.is_empty():
            print("Stack is Empty \n")
        else:
            val = self.stack[-1]
        return val
    
    def traverse(self):
        print(self.stack)
        
        
def main():
    st = Stack()
    
    st.push(1)
    st.push(4)
    st.push(2)
    st.push(55)
    st.push(34)
    
    st.traverse()
    
    st.pop()
    st.traverse()
    
    
    print("Empty" if st.is_empty() else "Not Empty")
    
    
main()

class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
        
class LinkList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        
    def push(self, value):
        new_node = Node(value)
        if self.head == None :
            self.head = self.tail = new_node;

        else:
            self.tail.next = new_node;
            self.tail = self.tail.next;
        print(f"inserted new node :{value} at end \n");
        
    def insert(self, index, value):
        new_node = Node(value)
        
        if index == 1:
            if self.head == None:
                self.push(value);
            else:
                new_node.next = self.head
                self.head = new_node
            print(f"Inserted {value} at index : {index} \n")
            return
        else:
            trav = self.head
            prev = None
            for i in range(0,index):
                if trav == None and (index - i) >= 2 :
                    print(f"User Trying to insert at invalid index : {index}")
                    return
                elif i == index-1:
                    prev.next = new_node
                    new_node.next = trav
                    print(f"Inserted {value} at index : {index} \n")
                    return
                    
                prev = trav
                trav =trav.next
                
    def pop(self):
        if self.head == self.tail:
            self.head  = self.tail = None;
            print("List Get Empty !!\n")
            return
        else:
            trav = self.head
            prev = None
            
            while trav.next:
                prev =trav
                trav = trav.next;
            
            prev.next = None;
            print(f"Removed Last Element : {self.tail.data}\n")
            self.tail = prev;
    
    def front(self):
        if self.head is not None:
            return self.tail.data;
        else:
            print("Empty List \n")
            return -1;
            
    def traversal(self):
        trav_node = self.head
        
        while trav_node:
            print(f"{trav_node.data} -> " , end = "")
            trav_node = trav_node.next
        print("\n")
            
def main():
    ll = LinkList()
    
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    
    ll.insert(3,10)
    ll.insert(1,20)
    ll.insert(8,40)
    
    
    ll.pop()
    ll.pop()
    
    ll.traversal()

main()

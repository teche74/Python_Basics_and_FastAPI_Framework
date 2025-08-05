class HashTable:
    def __init__(self, size):
        self.size = size
        self.map = [[] for _ in range(0,size)]
    
    def __hash(self, value):
        return hash(value) % self.size
    
    def put(self,key,value):
        index = self.__hash(key)
        
        for i ,(k,v) in enumerate(self.map[index]):
            if(k == key):
                self.map[index][i] = (key,value)
                return
        
        self.map[index].append((key,value))
    
    def get(self,key):
        index = self.__hash(key)
        for i ,(k,v) in enumerate(self.map[index]):
            if(k == key):
                return v
        return None
    
    def remove(self,key):
        index = self.__hash(key)
        
        for i ,(k,v) in enumerate(self.map[index]):
            if(k == key):
                del self.map[index][i]
                
    def contains(self,key):
        index = self.__hash(key)
        
        for i ,(k,v) in enumerate(self.map[index]):
            if(k == key):
                return True
        return False
    
    def values(self):
        vals = []
        for bucket in self.map:
            for _, v in bucket:
                vals.append(v)
        return vals
        
    def keys(self):
        kys = []
        
        for bucket in self.map:
            for k,_ in bucket:
                kys.append(k)
        return kys
        
    def traverse(self):
        for bucket in self.map:
            for key, value in bucket:
                print(f"{key} : {value}")
                
                
ht = HashTable(5)
ht.put("name", "Ujjwal")
ht.put("age", 21)
ht.put("lang", "Python")
ht.put("name", "Updated")

print("Get name:", ht.get("name")) 
print("Contains 'age':", ht.contains("age")) 
ht.remove("age")
print("Contains 'age':", ht.contains("age")) 

print("Keys:", ht.keys())
print("Values:", ht.values())
print("Traverse:")
ht.traverse()

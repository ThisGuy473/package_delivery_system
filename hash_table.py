#Creates a HashTable
class HashMap:
    
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size
    
    #Get hash index for key -> O(n)
    def _get_hash(self, key):
        hash = 0
        for item in str(key):
            hash += ord(item)
        return hash % self.size
    
    #insert key value pair into hash table -> O(n)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    
    #Delete hashtable key value pair using key -> O(n)
    def delete_value(self, key):
        key_hash = self._get_hash(key)
        
        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
    
    #Returns value using key -> O(n)
    def get_value(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    #returns all keys in hash table -> O(n)
    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0]) 
        print(arr) 

    #Prints all key value pairs to console -> O(n)
    def printer(self):
        for item in self.map:
            if item is not None:
                print(str(item))  
          
        

class KeyNode:
    def __init__(self, Key, Value):
        self.Key = Key
        self.Value = Value

class MyHashTable:
    def __init__(self):
        self.Array = []
        self.hSize = 128
        self.keysOcupied = 0
    
    def Constructor(self,hSize):
        self.Array = [None]*hSize
    
    def GetHashTableSize(self):
        return self.hSize
    
    def GetNumberOfKeys(self):
        return self.keysOcupied
    
    def HashFunction(self, key):
        sum = 0
        for i in key:
            num = ord(i)
            sum += num
        return sum%self.GetHashTableSize()
    
    def UpdateKey(self, key, value):
        index = self.HashFunction(key)
        keyN = KeyNode(key, value)
        
        if self.Array[index] == None:
            item = [keyN]
            self.Array[index] = item
            self.keysOcupied += 1
        else:
            self.Array[index].append(keyN)
                
    def SearchKey(self, key):
        for i in self.Array:
            if i.Key == key:
                return i.Value
        return 0
    
    def Rehash():
        pass
    
    
def main():
    table = MyHashTable()
    table.Constructor(128)
    
    table.UpdateKey("ABC", 12) 
    table.UpdateKey("ABC", 13)
    table.UpdateKey("ddd", 12) 
    table.UpdateKey("ttt", 13)
    
    
    for i in table.Array:
        if i != None:
            print(i)

if __name__ == "__main__":
    main()
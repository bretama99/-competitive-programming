class HashTable:
    def __init__(self):
        self.max_ = 100
        self.arr = [None]*self.max_
    def getHash(self,key):
        index = 0
        for char in key:
            index+=ord(char)
        return index%self.max_
    def __setitem__(self,key,val):
        h=self.getHash(key)
        self.arr[h] = val
    def __getitem__(self,key):
        h = self.getHash()
        return self.arr[h]

ht = HashTable()
print(ht.getHash('march 6'))
ht['march 6']=190
ht['march 5'] =890
ht['march 5']
print(ht.arr)
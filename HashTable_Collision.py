class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_Hash(self,key):
        for char in key:
            h = 0
            for char in key:
                h += ord(char)
            return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_Hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_Hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_Hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
t["march 1"] = 100
t["march 6"] = 110
t["march 17"] = 95
print(t.arr)
del t["march 17"]
print(t.arr)
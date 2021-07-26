class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_Hash(self,key):
        for char in key:
            h = 0
            for char in key:
                h += ord(char)
            return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_Hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_Hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_Hash(key)
        self.arr[h] = None

t = HashTable()
t['March 1'] = 100
t['March 10'] = 110
t['March 15'] = 95
print(t.arr)
del t['March 10']
print(t.arr)
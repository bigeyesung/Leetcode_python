from collections import OrderedDict

class LRUCache(object):
    def __init__(self, size):
        self.size, self.cache = size, OrderedDict()

    def get(self, key):
        for key1 in self.cache:
            print(self.cache[key1])
        value = self.cache.pop(key, -1)
        if value > 0: self.cache[key] = value
        for key1 in self.cache:
            print(self.cache[key1])
        return value


    
    def set(self, key, value):     
        if self.cache.pop(key, None) is None and self.size == len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value

def Main():
    cache = LRUCache(2)
    cache.set(1,1)
    cache.set(2,2)
    cache.get(1)
if __name__ == "__main__":
    Main()
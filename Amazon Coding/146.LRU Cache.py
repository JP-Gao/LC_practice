from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            # remove first, add back in
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # deleting existing key before refreshing it
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            # delete oldest (Least used)
            self.cache.popitem(last=False)
        self.cache[key] = value        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

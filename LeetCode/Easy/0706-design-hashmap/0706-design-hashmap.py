class MyHashMap:

    def __init__(self):
        self.store = {}

    def put(self, key: int, value: int) -> None:
        self.store[key] = value

    def get(self, key: int) -> int:
        if key in self.store:
            return self.store[key]
        
        return -1
        
    def remove(self, key: int) -> None:
        self.store.pop(key, None)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
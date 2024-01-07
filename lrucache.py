from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        # inicializar un mapa para guardar los key y values
        self.map = {}
        self.queue = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # get value from map and add key to the recently used queue
        if key in self.map:
            if len(self.queue) > 0:
                self.queue.remove(key)
            self.queue.append(key)
            return self.map[key]
        return -1   

    def put(self, key: int, value: int) -> None:
        if key in self.map: # update
            # delete from queue and append
            self.map[key] = value
            if len(self.queue) > 0:
                self.queue.remove(key)
            self.queue.append(key)
            # self.queue.append(key)
            return
        # if the key is not in map and the map is full then replace the leat used key in map
        # un stack con los keys
        if len(self.map) == self.capacity:
            keyToRemove = self.queue.popleft()
            self.map.pop(keyToRemove)
        self.map[key] = value
        self.queue.append(key)
        # self.map[]
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,"1")
obj.put(1,"1")
obj.put(2,"3")
obj.put(4,"1")
param_1 = obj.get(1)
print(param_1)
param_1 = obj.get(2)
print(param_1)
# obj.put(3,"3")
# param_1 = obj.get(2)
# print(param_1)
# param_1 = obj.get(3)
# print(param_1)

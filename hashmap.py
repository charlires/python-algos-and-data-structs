class MyHashMap(object):

    def __init__(self):
        self.elements = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.elements.insert(key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print(self.elements)
        try:
            return self.elements[key]
        except IndexError:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try: 
            self.elements.remove(key)
        except ValueError:
            return

# ["MyHashMap","put","put","get","get","put","get","remove","get"]
# [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
param_2 = obj.get(1)
print(param_2)
param_2 = obj.get(3)
print(param_2)
obj.put(2,1)
param_2 = obj.get(2)
print(param_2)
obj.remove(2)
param_2 = obj.get(2)
print(param_2)
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if self.head is None:
            return -1
        if index == 0:
            return self.head.val
        current_node = self.head
        counter = 0
        while (counter < index and current_node is not None):
            counter += 1
            current_node = current_node.next
        if (counter == index and current_node is not None):
            return current_node.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = self.head
        self.head = Node(val)
        self.head.next = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.head = Node(val)
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return
            
        counter = 0
        current_node = self.head
        while (counter < index-1 and current_node is not None):
            counter += 1
            current_node = current_node.next
            
        if counter == index -1 and current_node is not None:
            tmpnode = current_node.next
            current_node.next = Node(val)
            current_node.next.next = tmpnode

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0 and self.head is None:
            return
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return
        counter = 0
        current_node = self.head
        while (counter < index-1 and current_node is not None):
            counter += 1
            current_node = current_node.next
        if counter == index-1 and current_node is not None and current_node.next is not None:
            tmpnode = current_node.next
            current_node.next = tmpnode.next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(1)
# obj.addAtHead(1)
# obj.addAtTail(3)
obj.addAtIndex(1,0)
print(obj.get(0))
# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
print("")
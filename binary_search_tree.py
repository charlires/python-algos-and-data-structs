# from __future__ import annotations
from typing import Self


class Node:
    def __init__(self, value: int) -> None:
        self.val = value
        self.l = None
        self.r = None

    def insert(self, value: int) -> None:
        if value <= self.val:
            if self.l is None:
                self.l = Node(value)
            else:
                self.l.insert(value)
        else:
            if self.r is None:
                self.r = Node(value)
            else:
                self.r.insert(value)

    def contains(self, value: int) -> bool:
        if value < self.val and self.l is not None:
            return self.l.contains(value)
        elif value > self.val and self.r is not None:
            return self.r.contains(value)
        
        return value == self.val
    
    def pre_order_print(self) -> None:
        print(self.val)
        if self.l is not None:
            self.l.pre_order_print()
        if self.r is not None:
            self.r.pre_order_print()

    def delete(self, value: int, parent: Self) ->  None:
        if value < self.val:
            if self.l is not None:
                return self.l.delete(value, self)
            return False
        elif value > self.val:
            if self.r is not None:
                return self.r.delete(value, self)
            return False
        else: # elif value == self.val:
            if self.l is None and self.r is None:
                if parent is None:
                    self.val = None
                elif self == parent.l:
                    parent.l = None
                elif self == parent.r:
                    parent.r = None
            elif self.l is not None and self.r is None:
                if parent is None:
                    self.val = self.l.val
                    self.l.delete(self.val, self)   
                elif self == parent.l:
                    parent.l = self.l
                elif self == parent.r:
                    parent.r = self.l
            elif self.l is None and self.r is not None:
                if parent is None:
                    self.val = self.r.val
                    self.r.delete(self.val, self)   
                elif self == parent.l:
                    parent.l = self.r
                elif self == parent.r:
                    parent.r = self.r
            if self.l is not None and self.r is not None:
                self.val = self.l.find_max_value()
                self.l.delete(self.val, self)
            return True             

    def find_max_value(self):
        if self.r is None:
            return self.val
        return self.r.find_max_value()

head = Node(100)
head.insert(90)
head.insert(92)
head.insert(93)
head.insert(91)
head.insert(85)
head.insert(83)
head.insert(86)
head.pre_order_print()
print("-----------")
head.delete(100, None)
head.pre_order_print()
# print(head.contains(100))
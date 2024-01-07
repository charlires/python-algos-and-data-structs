# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        resultList = ListNode(0)
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) >= 1:
            resultList.next = lists[0]

        for list in lists[1:len(lists)]:
            if list is None:
                continue

            current_node = list
            while current_node is not None:
                resultList = self.addNode(current_node.val, resultList)
                current_node = current_node.next
        return resultList.next
    
    def addNode(self, val: int, resultList: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = resultList
        current_node = resultList.next
        while current_node is not None:
            if current_node.val >= val:
                previous_node.next = ListNode(val, current_node)
                return resultList
            if current_node.next is None:
                current_node.next = ListNode(val)
                return resultList 
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = ListNode(val)
        return resultList 
    
result = Solution().mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next

result = Solution().mergeKLists([ListNode(0), ListNode(1)])
current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next

result = Solution().mergeKLists([])
current_node = result
while current_node is not None:
    print(current_node.val)
    current_node = current_node.next
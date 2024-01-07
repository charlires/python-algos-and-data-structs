# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
import math

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        size = 0
        while node is not None:
            size += 1
            node = node.next
            
        mid = math.ceil(size / 2)
        node = head
        prev = None
        while mid > 1:
            prev = node
            node = node.next
            mid -= 1
        
        prev.next = node.next
        return head
    
Solution().deleteMiddle(ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6))))))))
# Solution().deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))

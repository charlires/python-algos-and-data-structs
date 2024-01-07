# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        nthnode = head
        nthnodeprev = None
        counter = 0
        while node is not None:
            if counter >= n:
                nthnodeprev = nthnode
                nthnode = nthnode.next
            counter += 1
            node = node.next

        if counter == 1:
            return None
        if n < counter:
            nthnodeprev.next = nthnode.next
            return head
        elif n == counter:
            return head.next 
        return head

# [1,2,3,4,5]
# Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
# Solution().removeNthFromEnd(ListNode(1), 1)
# Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 1)
# Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 2)
# Solution().removeNthFromEnd(None, 1)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        counter = 0
        current_node = head
        while current_node is not None:
            if "tail" in str(current_node.val):
                return current_node.val
            current_node.val = "tail connects to node index {}".format(counter)
            current_node = current_node.next
            counter += 1
        return "no cycle"
# [3,2,0,-4]
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next

print(Solution().hasCycle(head))
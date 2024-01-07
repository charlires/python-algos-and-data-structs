from collections import deque

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def bfs(head: Node) -> None:
    queue = deque()
    queue.append(head)
    while len(queue) > 0:
        current_node = queue.popleft()
        print(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

head = Node(1)
head.left = Node(2)
head.left.left = Node(3)
head.left.right = Node(4)
head.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)

bfs(head)
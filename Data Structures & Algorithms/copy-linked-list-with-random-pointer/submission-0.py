"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        def clone(node):
            if not node:
                return None
            
            if node in old_to_new:
                return old_to_new[node]
            
            new = Node(node.val)
            old_to_new[node] = new
            new.next = clone(node.next)
            new.random = clone(node.random)

            return new
        
        return clone(head)
        
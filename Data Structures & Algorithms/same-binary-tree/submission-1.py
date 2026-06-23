# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right


# bfs
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
        
#         queue = deque([p, q])
#         while queue:
#             n1, n2 = queue.popleft()
#             if n1.val != n2.val:
#                 return False
#             if n1.left and n2.left:
#                 queue.append([n1.left, n2.left])
#             if n1.right and n2.right:
#                 queue.append([n1.right, n2.right])
#         return True
    
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


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            p, q = q1.popleft(), q2.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            q1.append(p.left)
            q1.append(p.right)
            q2.append(q.left)
            q2.append(q.right)
        return True

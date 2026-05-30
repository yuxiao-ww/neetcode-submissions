# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(tr1, tr2):
            if not tr1 and not tr2:
                return True
            if not tr1 or not tr2 or tr1.val != tr2.val:
                return False
            return isSameTree(tr1.left, tr2.left) and isSameTree(tr1.right, tr2.right)
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
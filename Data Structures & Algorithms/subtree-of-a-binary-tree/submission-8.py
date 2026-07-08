# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSame(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot or root.val != subroot.val:
                return False
            
            return isSame(root.left, subroot.left) and isSame(root.right, subroot.right)
        
        if isSame(root, subRoot):
            return True
            
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r
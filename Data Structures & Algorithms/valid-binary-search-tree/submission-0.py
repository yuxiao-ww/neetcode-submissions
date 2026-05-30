# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vec = []

        def traversal(root):
            if not root:
                return
            
            traversal(root.left)
            vec.append(root.val)
            traversal(root.right)
        
        traversal(root)

        for i in range(len(vec)-1):
            if vec[i] >= vec[i+1]:
                return False
        
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        def dfs(node, value):
            if not node:
                return
            
            if node.val >= value:
                self.count += 1
            value = max(value, node.val)
            left = dfs(node.left, value)
            right = dfs(node.right, value)
        
        dfs(root, root.val)
        return self.count
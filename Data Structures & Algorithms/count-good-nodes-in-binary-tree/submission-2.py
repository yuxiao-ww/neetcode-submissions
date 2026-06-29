# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, value):
            if not node:
                return 0
            
            if node.val >= value:
                self.res += 1
                value = node.val
            left = dfs(node.left, value)
            right = dfs(node.right, value)
            return left + right
        
        dfs(root, root.val)
        return self.res

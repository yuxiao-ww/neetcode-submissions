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
                return
            if node.val >= value:
                self.res += 1
                value = node.val
            dfs(node.left, value)
            dfs(node.right, value)
        
        dfs(root, root.val)
        return self.res

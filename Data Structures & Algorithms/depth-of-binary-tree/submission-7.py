# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node):
            if not node:
                return 0
            
            left = getDepth(node.left)
            right = getDepth(node.right)
            return 1 + max(left, right)
        
        return getDepth(root)


# bfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

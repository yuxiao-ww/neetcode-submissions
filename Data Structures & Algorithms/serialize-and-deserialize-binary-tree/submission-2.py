# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        self.res = []
        def dfs(node):
            if not node:
                self.res.append("#")
                return
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        # print(self.res)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tree = data.split(",")
        self.i = 0
        def dfs():
            if tree[self.i] == "#":
                self.i += 1
                return None
            node = TreeNode(tree[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()






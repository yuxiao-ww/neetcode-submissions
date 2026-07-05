# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        seperate_idx = inorder.index(root_val)

        in_left = inorder[:seperate_idx]
        in_right = inorder[seperate_idx+1:]

        pre_left = preorder[1:len(in_left)+1]
        pre_right = preorder[len(in_left)+1:]

        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)

        return root

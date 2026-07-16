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

        inleft = inorder[:seperate_idx]
        inright = inorder[seperate_idx+1:]

        preleft = preorder[1:len(inleft)+1]
        preright = preorder[1+len(inleft):]

        root.left = self.buildTree(preleft, inleft)
        root.right = self.buildTree(preright, inright)

        return root
        

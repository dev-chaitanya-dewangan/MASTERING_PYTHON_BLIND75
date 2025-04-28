# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # RETURN NONE WHEN TREE IS EMPTY 
        if not root :return None
        # SWAP THE RIGHT SIDE OF CHILDREN WITH LEFT SIDE 
        root.left,root.right=root.right,root.left
        # RECURSIVELY SWAP THE CHILDRENS LEFT SIDE 
        self.invertTree(root.left)
        # RECURSIVELY SWAP THE CHILDRENS OF RIGHT SIDE 
        self.invertTree(root.right)

        return root
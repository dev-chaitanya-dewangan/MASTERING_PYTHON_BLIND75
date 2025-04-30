# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot :
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val==subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
        return False


"""
TIME COMPLEXITY:O(N) 
"""

"""
MTHOD TO SOLVE:
DFS->
FIRST WE CHECK WETHER SUBTREE IS EMPTY THEN RETURN TRUE IF YES
THEN RECURSIVELY CHECK
WETHER EACH SIDE IS SUBTREE -->WHERE WE CHECK IS BOTH SIDE SAME OR NOT 
THEN RETURN IF ABOVE RETURNS TRUE IF NOT RETURN FALSE
"""


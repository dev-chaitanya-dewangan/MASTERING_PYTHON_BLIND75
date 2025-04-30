# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # CHECKS ROOT IS SAME OR NOT
        if not p and not q:
            return True
        # IF ONE SIDE IS NONE OR NOT MATCHES WITH OTHER THEN IT RETURNS FALSE 
        if not p or not q or p.val != q.val:
            return False
        # IF ABOVE IS NOT TRIGGERED THEN 
        # THIS TRAVERSE FOR BOTH SIDE WETHER THEY MATCH OR NOT 
        # RETURN TRUE IF MATCHES ELSE FALSE
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

"""
TIME COMPLEXITY: O(P+Q) --> TRAVERSE FOR BOTH TREES
"""

"""
METHOD TO SOLVE :
WITH DEPTH FIRST SERACH -->
WE CHECK IF ALL THE CHILDRENS OF LEFT IS TRUE OR NOT 
AND ALSO CHEKC FOR RIGHT RIGHT 
IF BOTH ARE TRUE RETURN TRUE OR THEN RETURN FALSE
"""
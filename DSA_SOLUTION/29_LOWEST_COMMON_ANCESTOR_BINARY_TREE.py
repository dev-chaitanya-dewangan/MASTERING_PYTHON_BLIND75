# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur=root
        # LOOP THORUGH ALL NODES UNTIL FIND THE CORRECT GIVEN TWO NODE'S ANCESTOR
        while cur:
            # IF CURRENT NODE IS SMALLER THAN GIVEN TWO NODES THEN SHIFT POINTER TO RIGHT SIDE
            if p.val > cur.val and q.val >cur.val:
                cur=cur.right
            # IF CURRENT NODE IS SMALLER THAN GIVEN TWO NODES THEN SHIFT POINTER TO LEFT SIDE 
            elif p.val < cur.val and q.val <cur.val:
                cur=cur.left
            # ELSE WE HAVE FOUND THE ANCESTOR
            else:
                return cur


"""
TIME COMPLEXITY : O(N)
"""

"""
METHOD TO SOLVE :
THIS IS SPECIAL BINARY TREE(->which means left is less than current node and right is greater than current node)
FOR THIS WE ONLY CHECK WETHER GIVEN TWO P AND Q IS GREATER OR LESS THAN AND SHIFT THE POINTER TO THAT SIDE 
AND RETURN THE ANCESTOR.
"""
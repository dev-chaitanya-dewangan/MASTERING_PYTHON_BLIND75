# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # THIS IS GLOBAL RESULT 
        self.res=0

        # THIS RECURSIVELY ITERATE THE TREE AND REACHES THE LEAFS(last children of tree)
        # TAKES CHILDREN AS INPUT
        def dfs(curr):
            # THIS IS FOR LAST CHILDREN WHEN REACHES THAT RETURN ZERO
            if not curr:
                return 0
            # LEFT IS FOR ALL CHILDREN IN THIS SIDE
            left  =dfs(curr.left)
            # RIGHT IS FOR ALL CHILDREN IN THIS SIDE
            right = dfs(curr.right)
            # WHEN BOTH SIDES RECURSIVELY CHECKED THEN IT THIS UPDATES THE RESULT
            self.res=max(self.res,left+right)

            # THIS RETURN THE MAX DEPTH FROM EITHER OF THE SIDE (PLUS ONE IS FOR ->CURRENT NODE)
            return 1+max(left,right)
        # RESURSION FOR THE ROOT OF THE TREE
        dfs(root)
        return self.res


"""
TIME COMPLEXITY :O(N)
"""

"""
METHOD TO SOLVE THIS :
WITH DEPTH FIRST ALGORITHM CHECK THE MAX DEPTH OF THE CHIDLREN THEN RETURN 
THE LENGHT WHICH SIDE IS GREATER PLUS ONE FOR CURRENT NODE THEN COMPARE WITH RESULT AND RETURN THE MAX RESULT 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[[root,1]]
        # STORES RESULT 
        res=0
        # ITERATE UNTIL STACK IS EMPTY (in this loop we append until last or null )
        while stack:
            #SPLITTING THE REMOVED ELEMENT FROM "stack" -->NODE <tree> ,DEPTH <interger value of depth> 
            node,depth=stack.pop()
            #  IF CURRENT CHILD NOT HAVE ANY CHILDREN 
            # THEN INCREMENTS THE DEPTH AND APPEND THE CHILDRENS
            if node :
                # COMAPRES WHICH IS GREATER
                res=max(res,depth)
                # APPENDS LEFT CHILD  AND INCREMENTS DEPTH
                stack.append([node.left,depth+1])
                # APPENDS RIGHT CHILD   AND INCREMENTS DEPTH
                stack.append([node.right,depth+1])
        # RETURN THE RESULT
        return res


"""
TIME COMPLEXITY : O(N)

"""
"""
METHOD TO SOLVE THIS :
BY USING STACK APPEND UNTIL EACH CHILDREN HAVE IT'S OWN CHILDREN
AND BY SAME TIME REMOVE PREVIOUS CHILDREN FROM STACK ALSO INCREMENT DEPTH BY ONE  
UNTIL ITS EMPTY THEN RETURN THE RESULT
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        if not root :
            return res
        queue=[root]
        
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                node=queue.pop(0)
                # ONLY ADD TO RESULT IF IT IS LAST ->WHICH IS RIGHT MOST NODE
                if i==level_size-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


"""
TIME COMPLEXITY:(N)
"""

"""
MEHTOD TO SOLVE THIS 
FOR EVERY LEVEL WE ONLY ADD THE LAST NODE 
THEN ITERATE UNTIL THE LEAFS OF TREE
"""
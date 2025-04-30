# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # STORES RESULT
        res=[]
        # IF TREE IS EMPTY THEN RETURN EMPTY RESULT
        if not root:
            return res
        # THIS IS QUEUE FOR BFS ALGORITHM
        queue=[root]
        # LOOP UNTIL QUEUE IS EMPTY 
        while queue:
            # LEVEL STORES THE CURRENT QUEUE'S NODES VALUE
            level=[]
            # NEXT_QUE STORES THE BOTH LEFT AND RIGHT CHILDREN NODES
            next_que=[]
            # ITERATE FOR EVERY NODE IN  QUEUEU UNTIL IT IS EMPTY (this is for  )
            for node in queue:
                # APPEND THE CURRENT LEVEL NODE'S VALUE
                level.append(node.val)
                # IF LEFT IS PRESENT THEN APPEND IT 
                if node.left:
                    next_que.append(node.left)
                #SAME FOR THE RIGHT 
                if node.right:
                    next_que.append(node.right)
            # APPEND CURRENT LEVEL IN THE RESULT
            res.append(level)
            # UPDATE PREVIOUS LEVEL QUEUE TO NEW NEXT QUEUE
            queue=next_que    
        return res


"""
TIME COMPLEXITY :O(N)
"""

"""
MEHTOD TO SOLVE THIS :
ITERATE EVERY LEVEL AND ADD THE CURRENT NODE'S VALUE
"""
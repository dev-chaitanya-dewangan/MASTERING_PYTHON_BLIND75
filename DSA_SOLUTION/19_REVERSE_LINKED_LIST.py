# Class ListNode():
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
-----------------------------------------------------------------
ITERATIVE APPROACH
-----------------------------------------------------------------
"""
def reverseList(head):
    # START WITH "prev" VALUE OF NONE AND "curr" VALUE WITH HEAD 

    prev,curr=None,head
    # UNTIL THE CURRENT VALUE ISN'T NONE ITERATE
    while curr:
        # THIS TEMPORARY  STORES NEXT VALUE OF CURRENT 
        temp = curr.next
        # FOR NEXT VALUE OF CURRENT IT CHANGES TO PREV (reversing the pointing order)
        curr.next = prev 
        # FOR PREVIOUS NODE IT CHANGES IT TO CURRENT NODE 
        prev = curr 
        # 
        # THEN  CURRENT NODE IS ASSIGN TO TEMPORARY VALUE 
        curr= temp 
    # THEN RETURN THE PREVIOUS VALUE 
    return prev



"""
-----------------------------------------------------------------
TIME COMPLEXITY :O(N)
SPACE COMPLEXITY :O(1)
"""

"""

METHOD TO SOLVE THIS :

WE ARE ITERATIVELY TAKING CURRENT NODE ,ASSIGNING ITS ".next" TO PREVIOUS NODE THEN SHIFTING BOTH "PREVIOUS" AND "CURRENT"

"""

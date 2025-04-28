# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # DUMMY NODE WHICH POINTS HEAD (it is for the before index of the wanted deletion of node)
        dummy=ListNode(0,head)
        # STARTS POINTER FROM DUMMY NODE
        left=dummy
        # RIGHT POINTER STARTS FROM "nTH " POSITION
        right=head
        while n > 0:
            right=right.next
            n -=1
        #THIS LOOP ITERATE UNTIL RIGHT REACHES THE END OF LINKED LIST
        # AND INCREMENT THE POINTER BY ONE (BOTH) 
        while right:
            left=left.next
            right = right.next
        # WHEN WE HAVE REACH THE END OF LIST THEN SHIFT THE POINTER OF LEFT NODE TO NEXT(SKIPPING THE NEXT)
        left.next=left.next.next
        # RETURN HEAD OF THE LINKED LIST 
        return dummy.next


"""
TIME COMPLEXITY :O(N)
"""
"""
MEHTOD TO SOLVE THIS 
SHIFT RIGHT POINTER TILL GIVEN NTH POSITION THEN 
ITERATE BOTH POINTER UNTIL RIGHT POINTER REACHES THE END 
THEN SHIFT THE POINTER OF LEFT SKIPPING THE NEXT NODE
"""

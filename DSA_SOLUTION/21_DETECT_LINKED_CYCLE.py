def detectCycle(head):
    # DEFINE TWO POINTER ---> WHICH IS GOING TO BE FRIST INCREMENT BY ONE AND SECOND BY TWO
     fast,slow=head,head
    #  ITERATE UNTIL FAST REACHES END(None)
    while fast and fast.next
        # INCREMENT POINTER BY ONE
        slow=slow.next
        # INCREMENT POINTER BY TWO 
        fast=fast.next.next
        # CHECK IF FAST IS POINTING TWORDS THE SLOW THEN RETURN TRUE(we have found the cycle)
        if slow==fast:
            return True
    return False

"""
TIME COMPLEXITY  :O(N)
SPACE COMPLEXITY :O(1)

"""

"""
------------------------------------------------------------------------
METHOD TO SOLVE THIS
------------------------------------------------------------------------
THIS APPROACH USE TWO POINTER SLOW POINTER INCREMENT BY ONE AND FAST BY TWO --->
THEN CHECK WITH ITERATION IF FAST IS POITING TWORDS THE SLOW (if yes then return True || else return False)
"""
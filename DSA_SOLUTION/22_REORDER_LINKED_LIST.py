def reorderLinkedList(head):
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    second=slow.next
    prev=None
    slow.next=None
    while second:
        tmp=second.next
        second.next=prev
        prev=second
        second=tmp
    first,second=head,prev
    while second:
        t1,t2=first.next,second.next
        first.next=second
        second.next=t1
        first,second=t1,t2





"""
TIME COMPLEXITY :O(N)
SPACE COMPLEXITY :O(1)

"""

"""
--------------------------------------------------------------------------------------------------------------------------------
PSUEDO CODE 
--------------------------------------------------------------------------------------------------------------------------------
METHOD TO SOLVE THIS :
FIRST FIND MIDDLE(WITH SLOW AND FAST POINTER ) THEN SLPIT THE SECOND HALF --->
AND REVERSE SECOND HALF AND THEN MERGE BOTH LINKED LIST 
"""

























class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

def createLinkedList(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

head = createLinkedList([i for i in  range(0,21,3)])
print("Before reorder:")
printList(head)

reorderLinkedList(head)

print("After reorder:")
printList(head)
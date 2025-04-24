class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoSortedList(list1, list2):
    # Create a dummy node to serve as the start of the merged list
    dummy = node = ListNode()

    # Traverse both lists while neither is exhausted
    while list1 and list2:
        # Compare current nodes and attach the smaller one to the merged list
        if list1.val < list2.val:
            node.next = list1  # Attach list1 node
            list1 = list1.next  # Move list1 pointer forward
        else:
            node.next = list2  # Attach list2 node
            list2 = list2.next  # Move list2 pointer forward

        node = node.next  # Move node pointer forward in merged list

    # Attach the remaining nodes from the non-exhausted list
    node.next = list1 or list2

    # Return the head of the merged list (skipping the dummy node)
    return dummy.next

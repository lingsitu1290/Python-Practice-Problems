"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    
    # While there is a node, check to see if data is the same while traversing
    while headA and headB:
        if headA.data == headB.data:
            headA = headA.next
            headB = headB.next
        else:
            return 0
    
    # At the end of the linked list, both should equal to None
    if headA is None and headB is None:
        return 1
    return 0
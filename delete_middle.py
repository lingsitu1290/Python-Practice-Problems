'''
Delete a node in the middle of a linked list given only
access to that node
Original List : ->1->2->8->3->7->0->4
After Deleting the mid node (say 7) : ->1->2->8->3->0->4
'''

def delete_node(node):
    if node.next != None:
        node.next = node.next.data
        node.next = node.next.next
    else:
        node.data = None

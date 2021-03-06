"""Given linked list, reverse the nodes in this linked list in place.

For example:

    >>> ll = LinkedList(Node(1, Node(2, Node(3))))
    >>> reverse_linked_list_in_place(ll)
    >>> ll.as_string()
    '321'

"""


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    # Starting at the beginning of the linked list 
    current = lst.head 
    previous = None

    while current is not None: 
        nextNode = current.next

        # Redirect the pointer to the previous node
        current.next = previous

        # Reset previous to the current node 
        previous = current

        # Reset current to the nextNode 
        current = nextNode
    
    # Head will be reset to previous which is set to the current node 
    lst.head = previous

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
